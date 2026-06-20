# Feature Specification: Document Q&A

**Feature Branch**: `document-qa`

**Created**: 2026-06-20

**Status**: Implemented

**Input**: Core DocSage functionality — chat-based document Q&A with PDF and non-PDF sources.

## User Scenarios & Testing

### User Story 1 - Create and manage chats (Priority: P1)

Users create chat sessions to organize conversations around specific document sets.

**Why this priority**: Chats are the primary container for all sources and messages.

**Independent Test**: Create a chat, verify it appears in the sidebar, delete it and confirm removal.

**Acceptance Scenarios**:

1. **Given** the app is running, **When** the user creates a new chat, **Then** a new chat session appears in the sidebar.
2. **Given** an existing chat, **When** the user deletes it, **Then** the chat and its metadata are removed from the database.

### User Story 2 - Upload documents as sources (Priority: P1)

Users upload PDFs or other document types to ground answers in source content.

**Why this priority**: Source documents are required for meaningful Q&A.

**Independent Test**: Upload a `.txt` file, confirm it is stored and listed as a source for the active chat.

**Acceptance Scenarios**:

1. **Given** an active chat, **When** the user uploads a supported document, **Then** the document is processed and listed as a source.
2. **Given** a PDF upload, **When** processing completes, **Then** sections are stored under `sections/chat_{chat_id}/`.

### User Story 3 - Ask questions and receive answers (Priority: P1)

Users ask natural-language questions and receive answers grounded in uploaded or linked sources.

**Why this priority**: Q&A is the core value proposition of DocSage.

**Independent Test**: Upload a text file with known content, ask a question about it, verify the answer references that content.

**Acceptance Scenarios**:

1. **Given** a chat with indexed sources, **When** the user asks a question, **Then** an assistant response is displayed.
2. **Given** a chat with both PDF and non-PDF sources, **When** the user asks a question, **Then** answers are labeled by source type.

### User Story 4 - Add web links as sources (Priority: P2)

Users add URLs so page text can be indexed and queried like uploaded documents.

**Independent Test**: Add a URL, ask a question about its content, verify a grounded answer.

**Acceptance Scenarios**:

1. **Given** an active chat, **When** the user submits a valid URL, **Then** the page text is fetched and indexed in Chroma.

### Edge Cases

- Empty or unsupported file uploads should show a clear error.
- Invalid URLs should not crash the app.
- Chats without sources should prompt the user to add content before Q&A.

## Requirements

### Functional Requirements

- **FR-001**: System MUST persist chats, messages, and source metadata in SQLite.
- **FR-002**: System MUST route PDFs through structured-qa + llama.cpp (not Chroma).
- **FR-003**: System MUST route links and non-PDF files through Chroma + Gemini RAG.
- **FR-004**: System MUST support `.pdf`, `.txt`, `.docx`, `.csv`, `.html`, `.md`, and web links.
- **FR-005**: System MUST clean temporary upload files after processing.

### Key Entities

- **Chat**: A conversation session with a title and associated sources.
- **Source**: An uploaded document or web link attached to a chat.
- **Message**: A user question or assistant response in a chat thread.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can create a chat and upload a source in under 2 minutes.
- **SC-002**: Unit tests pass without API keys or local GGUF model.
- **SC-003**: Answers for non-PDF sources use Gemini RAG with similarity threshold 0.6.

## Assumptions

- Users have network access for Gemini API calls (non-PDF sources).
- Users provide a local GGUF model path for PDF Q&A.
- Single-user local deployment; no multi-user auth required.
