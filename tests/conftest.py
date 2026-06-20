import pytest

from db import connect_db, create_chat, init_schema


@pytest.fixture
def tmp_db_path(tmp_path):
    return tmp_path / "test.sqlite"


@pytest.fixture(autouse=True)
def isolated_db(monkeypatch, tmp_db_path):
    monkeypatch.setenv("DOC_SAGE_DB_PATH", str(tmp_db_path))
    conn = connect_db()
    init_schema(conn)
    conn.close()
    yield


@pytest.fixture
def chat_id():
    return create_chat("Test chat")
