# DocSage — RAG Chatbot

Single-module Streamlit app. Starter pytest unit tests in `tests/`.

## Quickstart

```bash
pip install -r requirements.txt

# One-time DB init
python create_relational_db.py

# Launch
streamlit run chats.py
```

## Testing

```bash
pip install -r requirements-dev.txt
pytest
```

Tests use a temporary SQLite file via `DOC_SAGE_DB_PATH` — no `.env`, API keys, or GGUF model needed for unit tests. Pre-commit also runs pytest when dev deps are installed.

## Environment

- Uses `django-environ` (not `python-dotenv`).
- Requires `.env` with:
  - `GOOGLE_API_KEY` — Gemini RAG for links and non-PDF files
  - `LLAMA_MODEL_PATH` — local GGUF model for PDF Q&A
- Do not commit `.env` or real secrets.

## Key structure

| Path | Purpose |
|---|---|
| `chats.py` | Entrypoint — Streamlit UI and routing |
| `db.py` | SQLite CRUD (`doc_sage.sqlite`) |
| `vector_functions.py` | ChromaDB + Gemini RAG for non-PDF sources |
| `structured_functions.py` | PDF section extraction + llama.cpp Q&A (Mozilla structured-qa) |
| `create_relational_db.py` | Schema definition (run once) |
| `tests/` | Pytest unit tests |
| `pytest.ini` | Pytest configuration |
| `requirements-dev.txt` | Dev dependencies (pytest) |
| `sections/` | PDF section files (`chat_{chat_id}/{doc_name}/`) |
| `persist/` | ChromaDB vector store (collections: `chat_{chat_id}`) |
| `temp_files/` | Temp uploads (cleaned after processing) |

## Gotchas

- PDFs use structured-qa (PyMuPDF4LLM + llama.cpp), not Chroma.
- Links and non-PDF files use Chroma + Gemini (`gemini-2.5-flash`, `gemini-embedding-001`).
- Chat collection names follow the pattern `chat_{chat_id}` in ChromaDB's `./persist/`.
- Document types: `.pdf` (structured), `.txt`, `.docx`, `.csv`, `.html`, `.md` (Chroma).
- Text splitting: `CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)`.
- Retriever: `similarity_score_threshold` at 0.6.
- llama.cpp model is cached in `st.session_state` after first PDF question.
- Old OpenAI Chroma embeddings are incompatible — wipe `./persist/` after migration.
