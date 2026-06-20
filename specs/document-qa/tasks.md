# Tasks: Document Q&A

**Input**: Design documents from `/specs/document-qa/`

**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 Create SQLite schema via `create_relational_db.py`
- [x] T002 [P] Configure `django-environ` for `.env` loading
- [x] T003 [P] Configure pytest with `DOC_SAGE_DB_PATH` in `tests/conftest.py`

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T004 Implement `db.py` CRUD for chats, sources, messages
- [x] T005 [P] Add unit tests in `tests/test_db.py`

**Checkpoint**: Foundation ready

## Phase 3: User Story 1 - Chat management (Priority: P1)

- [x] T006 [US1] Chat create/delete UI in `chats.py`
- [x] T007 [US1] Sidebar chat list and selection

## Phase 4: User Story 2 - Document upload (Priority: P1)

- [x] T008 [US2] File upload handler in `chats.py`
- [x] T009 [P] [US2] PDF pipeline in `structured_functions.py`
- [x] T010 [P] [US2] Non-PDF pipeline in `vector_functions.py`

## Phase 5: User Story 3 - Q&A (Priority: P1)

- [x] T011 [US3] Question routing by source type in `chats.py`
- [x] T012 [P] [US3] PDF Q&A via llama.cpp in `structured_functions.py`
- [x] T013 [P] [US3] Gemini RAG in `vector_functions.py`
- [x] T014 [US3] Tests in `tests/test_chats_helpers.py`, `tests/test_structured_functions.py`

## Phase 6: User Story 4 - Web links (Priority: P2)

- [x] T015 [US4] URL fetch and Chroma indexing in `vector_functions.py`

## Phase 7: Polish & Cross-Cutting Concerns

- [x] T016 Documentation: README.md, AGENTS.md, USER_MANUAL.md
- [x] T017 GitLab compliance: CI, pre-commit, Spec-Kit, LICENSE
- [x] T018 Run pytest and pre-commit
