# DocSage Constitution

Governing principles for DocSage development. All specifications, plans, and implementations must align with these rules.

## Core Principles

### Single-module Streamlit architecture

DocSage is a single-module Streamlit application. The entrypoint is `chats.py`; database, vector, and structured PDF logic live in sibling modules (`db.py`, `vector_functions.py`, `structured_functions.py`). Do not introduce unnecessary package hierarchies or frameworks.

### Dual Q&A pipelines

- **PDFs**: Use structured-qa (PyMuPDF4LLM + llama.cpp). Do not route PDF content through Chroma.
- **Links and non-PDF files**: Use per-chat Chroma collections with Gemini embeddings and RAG (`gemini-2.5-flash`, `gemini-embedding-001`).

### Testability without external services

Unit tests must run without `.env`, API keys, or a local GGUF model. Use `DOC_SAGE_DB_PATH` for a temporary SQLite database in tests.

### No secrets or runtime artifacts in version control

Never commit `.env`, real API keys, `doc_sage.sqlite`, `persist/`, `sections/`, `temp_files/`, or `__pycache__/`.

### AGPLv3 compliance

This project is licensed under the GNU Affero General Public License v3.0. Contributions and distributions must comply with AGPLv3 terms.

## Technology constraints

- Python 3.10+
- Environment variables via `django-environ` (not `python-dotenv`)
- Text splitting: `CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)`
- Retriever threshold: `similarity_score_threshold` at 0.6
- Chroma collection naming: `chat_{chat_id}` in `./persist/`

## Governance

- Constitution changes require updating dependent specs and plans.
- New features should follow Spec-Kit workflow: spec → plan → tasks → implement.
- Pre-commit and CI must pass before merge.

**Version**: 1.0.0 | **Ratified**: 2026-06-20 | **Last Amended**: 2026-06-20
