from db import (
    create_chat,
    create_message,
    create_source,
    delete_chat,
    delete_messages,
    delete_source,
    get_messages,
    list_chats,
    list_sources,
    read_chat,
    read_source,
    update_chat,
    update_source,
)


def test_create_and_read_chat():
    chat_id = create_chat("My Chat")
    chat = read_chat(chat_id)

    assert chat is not None
    assert chat[0] == chat_id
    assert chat[1] == "My Chat"


def test_list_chats():
    create_chat("First")
    create_chat("Second")

    titles = [chat[1] for chat in list_chats()]

    assert "First" in titles
    assert "Second" in titles


def test_update_chat():
    chat_id = create_chat("Old Title")
    update_chat(chat_id, "New Title")
    chat = read_chat(chat_id)

    assert chat[1] == "New Title"


def test_delete_chat():
    chat_id = create_chat("To Delete")
    delete_chat(chat_id)

    assert read_chat(chat_id) is None


def test_create_list_and_delete_source(chat_id):
    create_source("notes.txt", "hello", chat_id, source_type="document")
    create_source("https://example.com", "", chat_id, source_type="link")

    documents = list_sources(chat_id, source_type="document")
    links = list_sources(chat_id, source_type="link")

    assert len(documents) == 1
    assert documents[0][1] == "notes.txt"
    assert len(links) == 1
    assert links[0][1] == "https://example.com"

    delete_source(documents[0][0])
    assert list_sources(chat_id, source_type="document") == []


def test_read_and_update_source(chat_id):
    create_source("doc.txt", "original", chat_id)
    sources = list_sources(chat_id)
    source_id = sources[0][0]

    source = read_source(source_id)
    assert source[1] == "doc.txt"
    assert source[2] == "original"

    update_source(source_id, "renamed.txt", "updated")
    updated = read_source(source_id)
    assert updated[1] == "renamed.txt"
    assert updated[2] == "updated"


def test_create_get_and_delete_messages(chat_id):
    create_message(chat_id, "user", "Hello")
    create_message(chat_id, "ai", "Hi there")

    messages = get_messages(chat_id)
    assert messages == [("user", "Hello"), ("ai", "Hi there")]

    delete_messages(chat_id)
    assert get_messages(chat_id) == []
