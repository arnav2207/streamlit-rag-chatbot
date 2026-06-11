# DocSage — RAG Chatbot

Single-module Streamlit app. No packages, no tests, no linter/formatter/typechecker.

## Quickstart

```bash
# No requirements.txt — install manually
pip install streamlit langchain langchain-openai langchain-chroma langchain-community beautifulsoup4 requests django-environ

# One-time DB init
python create_relational_db.py

# Launch
streamlit run chats.py
```

## Environment

- Uses `django-environ` (not `python-dotenv`). Requires `.env` with `OPENAI_API_KEY`.
- **No `.gitignore` exists**. `.env` with real secrets is tracked — do not commit secrets.

## Key structure

| Path | Purpose |
|---|---|
| `chats.py` | Entrypoint — Streamlit UI and routing |
| `db.py` | SQLite CRUD (`doc_sage.sqlite`) |
| `vector_functions.py` | ChromaDB + LangChain RAG pipeline |
| `create_relational_db.py` | Schema definition (run once) |
| `persist/` | ChromaDB vector store (collections: `chat_{chat_id}`) |
| `temp_files/` | Temp uploads (cleaned after processing) |

## Gotchas

- **API key leak**: `vector_functions.py:29` prints `OPENAI_API_KEY` to stdout on import. Remove or guard before committing.
- Chat collection names follow the pattern `chat_{chat_id}` in ChromaDB's `./persist/`.
- Document types supported: `.txt`, `.pdf`, `.docx`, `.csv`, `.html`, `.md`.
- Text splitting: `CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)`.
- Retriever: `similarity_score_threshold` at 0.6.
- Uses `gpt-4o-mini`.
