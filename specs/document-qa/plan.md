# Implementation Plan: Document Q&A

**Branch**: `document-qa` | **Date**: 2026-06-20 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/document-qa/spec.md`

## Summary

Implement chat-based document Q&A in a Streamlit app with dual pipelines: PDF sources use structured-qa + llama.cpp locally; links and non-PDF files use per-chat Chroma collections with Gemini RAG.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: Streamlit, langchain, langchain-google-genai, langchain-chroma, structured-qa, ocrmypdf, django-environ

**Storage**: SQLite (`doc_sage.sqlite`), Chroma (`./persist/`), PDF sections (`./sections/`)

**Testing**: pytest with `DOC_SAGE_DB_PATH` for isolated SQLite

**Target Platform**: Local Streamlit web application

## Constitution Check

- [x] Aligns with single-module Streamlit architecture
- [x] Uses correct Q&A pipeline (PDF vs non-PDF)
- [x] Tests do not require API keys or GGUF model
- [x] No secrets or runtime artifacts committed
- [x] AGPLv3 compliant

## Project Structure

### Documentation (this feature)

```text
specs/document-qa/
├── spec.md
├── plan.md
└── tasks.md
```

### Source Code (repository root)

```text
chats.py                  # Streamlit UI, routing, uploads, chat flow
db.py                     # SQLite CRUD
vector_functions.py       # Chroma + Gemini RAG for non-PDF sources
structured_functions.py   # PDF preprocessing + llama.cpp Q&A
create_relational_db.py   # Schema setup
tests/
├── conftest.py
├── test_db.py
├── test_chats_helpers.py
└── test_structured_functions.py
```

**Structure Decision**: Flat module layout at repository root; no `src/` package. Streamlit entrypoint is `chats.py`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| — | — | — |
