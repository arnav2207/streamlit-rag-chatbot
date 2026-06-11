# DocSage Agent Skills

Use these skills when working on this repository. DocSage is a small Streamlit RAG chatbot that combines a SQLite relational store with per-chat Chroma collections and LangChain/OpenAI retrieval.

## Project Orientation

- Treat `chats.py` as the application entrypoint. It owns Streamlit routing, chat UI, upload/link ingestion, and calls into the database and vector helpers.
- Treat `db.py` as the SQLite CRUD boundary for `doc_sage.sqlite`.
- Treat `vector_functions.py` as the LangChain and Chroma boundary for document loading, splitting, embeddings, retrieval, and answer generation.
- Treat `create_relational_db.py` as the one-time schema initializer.
- Keep the current lightweight structure unless the user explicitly asks for a larger refactor.

## Environment And Safety

- Use `django-environ`, not `python-dotenv`.
- Expect `.env` to contain `OPENAI_API_KEY`.
- Do not print, expose, commit, or copy secrets. If secret logging appears, remove or guard it before committing.
- There is no dependency manifest. If dependencies are needed, document manual `pip install` commands instead of assuming `requirements.txt`.
- Avoid committing generated or local runtime data such as `doc_sage.sqlite`, `persist/`, `temp_files/`, `__pycache__/`, and `.env`.

## Streamlit App Skill

When changing the UI or chat workflow:

- Preserve URL routing through `st.query_params` with `chat_id`.
- Keep chat creation, chat listing, document upload, link ingestion, and message display understandable from a single Streamlit flow.
- Store user and assistant messages through `create_message`.
- Use existing database helpers rather than opening SQLite connections from `chats.py`.
- Keep sidebar source management scoped to the active chat.
- Be careful with `st.rerun()` and `st.session_state`; avoid loops or stale widget state.

## SQLite Skill

When changing persistent relational data:

- Update `create_relational_db.py` for schema changes.
- Update `db.py` with focused helper functions for all CRUD access.
- Use parameterized SQL for every user-controlled value.
- Preserve the table relationships:
  - `chat.id` owns chats.
  - `messages.chat_id` belongs to a chat.
  - `sources.chat_id` belongs to a chat.
- Remember that deleting a chat currently does not automatically delete its messages, sources, or vector collection unless code is added to do so.

## RAG And Vector Store Skill

When changing retrieval or ingestion:

- Use collection names in the form `chat_{chat_id}`.
- Keep Chroma persistence under `./persist` unless the user asks for a configurable path.
- Supported uploads are `.txt`, `.pdf`, `.docx`, `.csv`, `.html`, and `.md`.
- Document loading belongs in `load_document`.
- Text splitting currently uses `CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)`.
- Retrieval currently uses `similarity_score_threshold` with a default threshold of `0.6`.
- The LLM is currently `gpt-4o-mini`.
- If changing embeddings, model names, chunking, or retrieval thresholds, check how existing persisted collections will behave.

## Web Link Ingestion Skill

When changing link support:

- Fetch links with a browser-like `User-Agent` unless there is a reason to change it.
- Parse HTML with BeautifulSoup and store clean text in a LangChain `Document`.
- Preserve source metadata such as the original URL when adding link content to Chroma.
- Handle inaccessible, empty, or non-HTML responses gracefully in the Streamlit UI.

## Verification Skill

This project has no tests, linter, formatter, or typechecker configured. Use lightweight verification:

- Run `python create_relational_db.py` when schema behavior changes.
- Run `python -m py_compile chats.py db.py vector_functions.py create_relational_db.py` after Python edits.
- Run `streamlit run chats.py` for manual end-to-end checks when UI or ingestion behavior changes.
- For RAG changes, manually verify a chat can ingest a small document and answer a question grounded in that document.

## Change Style

- Make small, direct edits that match the existing procedural style.
- Prefer clear helper functions over new frameworks or broad abstractions.
- Keep comments useful and brief.
- Do not introduce a package layout, dependency manager, test framework, formatter, or linter unless the user asks.
- If adding cleanup behavior, be explicit about whether it affects SQLite rows, Chroma collections, temp files, or all of them.

