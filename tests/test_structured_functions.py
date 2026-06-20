import os

from structured_functions import (
    get_sections_dir,
    is_llama_model_configured,
    is_pdf_source,
)


def test_is_pdf_source():
    assert is_pdf_source("report.pdf") is True
    assert is_pdf_source("REPORT.PDF") is True
    assert is_pdf_source("notes.txt") is False
    assert is_pdf_source("data.csv") is False


def test_get_sections_dir():
    path = get_sections_dir(42, "lecture.pdf")
    assert path == os.path.join("./sections", "chat_42", "lecture.pdf")


def test_is_llama_model_configured_without_env(monkeypatch):
    monkeypatch.delenv("LLAMA_MODEL_PATH", raising=False)
    assert is_llama_model_configured() is False


def test_is_llama_model_configured_with_env(monkeypatch):
    monkeypatch.setenv("LLAMA_MODEL_PATH", "/path/to/model.gguf")
    assert is_llama_model_configured() is True
