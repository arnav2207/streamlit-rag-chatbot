import os
import shutil

import environ
import streamlit as st

env = environ.Env()
environ.Env.read_env()

SECTIONS_ROOT = "./sections"
TEMP_DIR = "temp_files"
TESSERACT_INSTALL_MSG = (
    "Tesseract OCR is required for scanned/image PDFs. Install it with:\n"
    "  macOS:   brew install tesseract\n"
    "  Ubuntu:  sudo apt install tesseract-ocr"
)


def get_sections_dir(chat_id, doc_name: str) -> str:
    return os.path.join(SECTIONS_ROOT, f"chat_{chat_id}", doc_name)


def is_pdf_source(doc_name: str) -> bool:
    return doc_name.lower().endswith(".pdf")


def pdf_needs_ocr(file_path: str, min_chars: int = 20) -> bool:
    """Return True when a PDF has little or no embedded text (likely scanned)."""
    import fitz

    doc = fitz.open(file_path)
    text = "".join(page.get_text() for page in doc)
    doc.close()
    return len(text.strip()) < min_chars


def prepare_pdf_with_ocr(file_path: str) -> tuple[str, str | None]:
    """
    OCR image-only PDF pages so pymupdf4llm can extract text.

    Skips OCR when the PDF already has extractable text.
    Returns (path_for_extraction, ocr_temp_path_to_cleanup).
    """
    if not pdf_needs_ocr(file_path):
        return file_path, None

    import ocrmypdf
    from ocrmypdf.exceptions import MissingDependencyError

    os.makedirs(TEMP_DIR, exist_ok=True)
    basename = os.path.basename(file_path)
    ocr_path = os.path.join(TEMP_DIR, f"{basename}.ocr.pdf")

    try:
        ocrmypdf.ocr(
            file_path,
            ocr_path,
            skip_text=True,
            progress_bar=False,
        )
        return ocr_path, ocr_path
    except MissingDependencyError as e:
        raise RuntimeError(f"{TESSERACT_INSTALL_MSG}\n\nDetails: {e}") from e
    except Exception as e:
        print(f"OCR skipped, using original PDF: {e}")
        if os.path.exists(ocr_path):
            os.remove(ocr_path)
        return file_path, None


def process_pdf_to_sections(file_path: str, chat_id, doc_name: str) -> list[str]:
    sections_dir = get_sections_dir(chat_id, doc_name)
    os.makedirs(os.path.dirname(sections_dir), exist_ok=True)

    pdf_for_extraction, ocr_temp_path = prepare_pdf_with_ocr(file_path)
    try:
        from structured_qa.preprocessing import document_to_sections_dir

        return document_to_sections_dir(pdf_for_extraction, sections_dir)
    finally:
        if ocr_temp_path and os.path.exists(ocr_temp_path):
            os.remove(ocr_temp_path)


def remove_pdf_sections(chat_id, doc_name: str) -> None:
    sections_dir = get_sections_dir(chat_id, doc_name)
    if os.path.isdir(sections_dir):
        shutil.rmtree(sections_dir)


def get_pdf_sections_dirs(chat_id, pdf_source_names: list[str]) -> list[str]:
    dirs = []
    for name in pdf_source_names:
        sections_dir = get_sections_dir(chat_id, name)
        if os.path.isdir(sections_dir):
            dirs.append(sections_dir)
    return dirs


def load_llama_model(model_path: str):
    """
    Load a GGUF model from a local file path or HuggingFace id (org/repo/filename).
    structured-qa's load_llama_cpp_model only supports the HuggingFace format.
    """
    from llama_cpp import Llama
    from structured_qa.model_loaders import LlamaModel, gpu_available

    if os.path.isfile(model_path):
        model = Llama(
            model_path=model_path,
            n_ctx=0,
            verbose=False,
            n_gpu_layers=-1 if gpu_available() else 0,
        )
        return LlamaModel(model=model)

    parts = model_path.split("/")
    if len(parts) == 3 and not model_path.startswith("/"):
        from structured_qa.model_loaders import load_llama_cpp_model

        return load_llama_cpp_model(model_path)

    raise FileNotFoundError(
        "LLAMA_MODEL_PATH must be an existing local .gguf file or a HuggingFace id "
        f"in org/repo/filename format. Got: {model_path}"
    )


def get_llama_model():
    if "llama_model" in st.session_state:
        return st.session_state.llama_model

    if st.session_state.get("llama_model_error"):
        return None

    model_path = env("LLAMA_MODEL_PATH", default=None)
    if not model_path:
        return None

    try:
        model = load_llama_model(model_path)
        st.session_state.llama_model = model
        return model
    except (FileNotFoundError, ValueError, OSError) as e:
        st.session_state.llama_model_error = str(e)
        return None


def get_llama_model_error() -> str | None:
    return st.session_state.get("llama_model_error")


def is_llama_model_configured() -> bool:
    return bool(env("LLAMA_MODEL_PATH", default=None))


def is_llama_model_loaded() -> bool:
    return "llama_model" in st.session_state


def answer_from_pdf_sections(question: str, sections_dirs: list[str]) -> str | None:
    from structured_qa.config import ANSWER_PROMPT, FIND_PROMPT
    from structured_qa.workflow import find_retrieve_answer

    model = get_llama_model()
    if model is None:
        return None

    for sections_dir in sections_dirs:
        answer, _ = find_retrieve_answer(
            question=question,
            model=model,
            sections_dir=sections_dir,
            find_prompt=FIND_PROMPT,
            answer_prompt=ANSWER_PROMPT,
        )
        if answer and answer.strip():
            return answer.strip()

    return None
