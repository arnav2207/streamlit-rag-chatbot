from unittest.mock import patch

from db import create_source
from chats import (
    generate_chat_response,
    get_pdf_source_names,
    has_non_pdf_sources,
    stream_response,
)


def test_get_pdf_source_names(chat_id):
    create_source("report.pdf", "", chat_id, source_type="document")
    create_source("notes.txt", "", chat_id, source_type="document")
    create_source("https://example.com", "", chat_id, source_type="link")

    assert get_pdf_source_names(chat_id) == ["report.pdf"]


def test_has_non_pdf_sources_pdf_only(chat_id):
    create_source("report.pdf", "", chat_id, source_type="document")
    assert has_non_pdf_sources(chat_id) is False


def test_has_non_pdf_sources_link_only(chat_id):
    create_source("https://example.com", "", chat_id, source_type="link")
    assert has_non_pdf_sources(chat_id) is True


def test_has_non_pdf_sources_mixed(chat_id):
    create_source("report.pdf", "", chat_id, source_type="document")
    create_source("notes.txt", "", chat_id, source_type="document")
    assert has_non_pdf_sources(chat_id) is True


def test_has_non_pdf_sources_empty(chat_id):
    assert has_non_pdf_sources(chat_id) is False


@patch("chats.time.sleep")
def test_stream_response(mock_sleep):
    chunks = list(stream_response("hello world"))
    assert chunks == ["hello ", "world "]
    mock_sleep.assert_called()


def test_generate_chat_response_no_context(chat_id):
    response = generate_chat_response(chat_id, "What is this about?")
    assert response == "I need some context to answer that question."
