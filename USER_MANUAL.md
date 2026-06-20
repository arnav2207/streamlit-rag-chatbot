# DocSage User Manual

DocSage is a Streamlit document Q&A application. Create chat sessions, add documents or web links as sources, and ask questions answered from that content.

## Prerequisites

- Python 3.10 or newer
- Google Gemini API key (for links and non-PDF documents)
- Local GGUF model file for PDF Q&A (recommended: Qwen2.5-3B-Instruct)
- ~10 GB RAM recommended for local PDF Q&A
- Tesseract OCR for scanned/image PDFs:
  - macOS: `brew install tesseract`
  - Ubuntu/Debian: `sudo apt install tesseract-ocr`

## Installation

```bash
pip install -r requirements.txt
```

On macOS, if `llama-cpp-python` fails to install:

```bash
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python
```

## Configuration

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
LLAMA_MODEL_PATH=path/to/model.gguf
```

Do not share or commit your `.env` file.

## Database setup

Initialize the SQLite database once:

```bash
python create_relational_db.py
```

## Running the app

```bash
streamlit run chats.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`).

## Using DocSage

1. **Create a chat** — Start a new conversation from the sidebar.
2. **Add sources** — Upload documents or paste web links for the active chat.
3. **Ask questions** — Type questions in the chat input; answers are drawn from your sources.

## Supported sources

| Type | Pipeline |
| --- | --- |
| `.pdf` | OCR (if needed) → structured sections → local llama.cpp Q&A |
| `.txt`, `.docx`, `.csv`, `.html`, `.md` | Chroma embeddings + Gemini RAG |
| Web links | Fetched and indexed in Chroma with Gemini |

## Mixed-source chats

If a chat has both PDFs and other sources, answers appear in two labeled sections: one from PDF sources (local llama.cpp) and one from other sources (Gemini RAG).

## Troubleshooting

- **PDF answers fail**: Confirm `LLAMA_MODEL_PATH` points to a valid GGUF file and you have enough RAM.
- **Link/non-PDF answers fail**: Confirm `GOOGLE_API_KEY` is set and valid.
- **Scanned PDFs not working**: Install Tesseract OCR and ensure `ocrmypdf` is available.
- **Stale embeddings after migration**: Delete `./persist/` and re-upload non-PDF sources.

## Getting help

See [README.md](README.md) for project structure and development notes. For contributions, see [CONTRIBUTING.md](CONTRIBUTING.md).
