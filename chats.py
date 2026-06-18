import streamlit as st
import os
import time
import math
import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from db import (
    read_chat,
    create_chat,
    list_chats,
    delete_chat,
    create_message,
    get_messages,
    create_source,
    list_sources,
    delete_source,
)

from vector_functions import (
    load_document,
    create_collection,
    load_retriever,
    generate_answer_from_context,
    add_documents_to_collection,
    load_collection,
)
from structured_functions import (
    is_pdf_source,
    process_pdf_to_sections,
    remove_pdf_sections,
    get_pdf_sections_dirs,
    answer_from_pdf_sections,
    is_llama_model_configured,
    is_llama_model_loaded,
    get_llama_model_error,
)


def get_pdf_source_names(chat_id):
    documents = list_sources(chat_id, source_type="document")
    return [doc[1] for doc in documents if is_pdf_source(doc[1])]


def has_non_pdf_sources(chat_id):
    documents = list_sources(chat_id, source_type="document")
    links = list_sources(chat_id, source_type="link")
    non_pdf_docs = [doc for doc in documents if not is_pdf_source(doc[1])]
    return bool(non_pdf_docs or links)


def generate_chat_response(chat_id, prompt):
    pdf_dirs = get_pdf_sections_dirs(chat_id, get_pdf_source_names(chat_id))
    pdf_answer = None
    rag_answer = None

    if pdf_dirs:
        if not is_llama_model_configured():
            pdf_answer = "PDF sources are indexed locally, but LLAMA_MODEL_PATH is not configured."
        else:
            pdf_answer = answer_from_pdf_sections(prompt, pdf_dirs)
            if pdf_answer is None:
                model_error = get_llama_model_error()
                if model_error:
                    pdf_answer = f"Could not load llama.cpp model: {model_error}"
                else:
                    pdf_answer = (
                        "I could not find an answer in the uploaded PDF sources."
                    )

    collection_name = f"chat_{chat_id}"
    if has_non_pdf_sources(chat_id) and os.path.exists("./persist"):
        retriever = load_retriever(collection_name=collection_name)
        rag_answer = generate_answer_from_context(retriever, prompt)

    if pdf_answer and rag_answer:
        return f"From PDF sources:\n{pdf_answer}\n\nFrom other sources:\n{rag_answer}"
    if pdf_answer:
        return pdf_answer
    if rag_answer:
        return rag_answer
    return "I need some context to answer that question."


def chats_home():
    st.markdown(
        "<h1 style='text-align: center;'>DocSage🧙‍♂️</h1>", unsafe_allow_html=True
    )

    with st.container(border=True):
        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            chat_title = st.text_input(
                "Chat Title", placeholder="Enter Chat Title", key="chat_title"
            )

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add vertical space
            if st.button("Create Chat", type="primary"):
                if chat_title:
                    chat_id = create_chat(chat_title)
                    st.success(f"Created new chat: {chat_title}")
                    st.query_params.from_dict({"chat_id": chat_id})
                    st.rerun()
                else:
                    st.warning("Please enter a chat title")

    with st.container(border=True):
        st.subheader("Previous Chats")

        # get previous chats from db
        previous_chats = list_chats()

        # Pagination settings
        chats_per_page = 5
        total_pages = math.ceil(len(previous_chats) / chats_per_page)

        # Get current page from session state
        if "current_page" not in st.session_state:
            st.session_state.current_page = 1

        # Calculate start and end indices for the current page
        start_idx = (st.session_state.current_page - 1) * chats_per_page
        end_idx = start_idx + chats_per_page

        # Display chats for the current page
        for chat in previous_chats[start_idx:end_idx]:
            chat_id, chat_title = chat[0], chat[1]
            with st.container(border=True):
                col1, col2, col3 = st.columns([0.6, 0.2, 0.2])

                with col1:
                    st.markdown(f"**{chat_title}**")
                with col2:
                    if st.button("📂 Open", key=f"open_{chat_id}"):
                        st.query_params.from_dict({"chat_id": chat_id})
                        st.rerun()

                with col3:
                    if st.button("🗑️ Delete", key=f"delete_{chat_id}"):
                        delete_chat(chat_id)
                        st.success(f"Deleted chat: {chat_title}")
                        st.rerun()

        # Pagination controls
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            if st.button("Previous") and st.session_state.current_page > 1:
                st.session_state.current_page -= 1
                st.rerun()
        with col2:
            st.write(f"Page {st.session_state.current_page} of {total_pages}")
        with col3:
            if st.button("Next") and st.session_state.current_page < total_pages:
                st.session_state.current_page += 1
                st.rerun()


def stream_response(response):
    """
    Stream a response word by word with a delay between each word.
    Args:
        response (str): The text response to stream
    Yields:
        str: Individual words from the response with a space appended
    Note:
        Adds a 50ms delay between each word to create a typing effect
    """

    # Split response into words and stream each one
    for word in response.split():
        # Yield the word with a space and pause briefly
        yield word + " "
        time.sleep(0.05)


def chat_page(chat_id):
    """
    Renders the main chats page where users can:
    - Create new chats with titles
    - View and manage previous chats
    - Navigate through paginated chat history

    The page displays a header, chat creation form, and list of existing chats
    with options to open each chat.
    """
    chat = read_chat(chat_id)

    if not chat:
        st.error("Chat not found")
        return

    # Retrieve messages from DB
    messages = get_messages(chat_id)

    # Display messages
    if messages:
        for sender, content in messages:
            if sender == "user":
                with st.chat_message("user"):
                    st.markdown(content)
            elif sender == "ai":
                with st.chat_message("assistant"):
                    st.markdown(content)
    else:
        st.write("No messages yet. Start the conversation!")

    # Add a text input for new messages
    prompt = st.chat_input("Type your message here...")
    if prompt:
        # Save user message
        create_message(chat_id, "user", prompt)

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response
        with st.spinner("Generating answer..."):
            response = generate_chat_response(chat_id, prompt)

        # Save AI response
        create_message(chat_id, "ai", response)

        # Display AI response
        with st.chat_message("assistant"):
            st.write_stream(stream_response(response))

        st.rerun()

    # Sidebar
    with st.sidebar:
        # Button to return to the main chats page
        if st.button("Back to Chats"):
            st.query_params.clear()
            st.rerun()

        # Chat name
        st.subheader(f"{chat[1]}")

        pdf_sources = get_pdf_source_names(chat_id)
        if pdf_sources:
            st.caption("PDF sources use local structured sections (llama.cpp).")
        if has_non_pdf_sources(chat_id):
            st.caption("Other sources use Chroma RAG (Gemini).")
        if is_llama_model_loaded():
            st.caption("llama.cpp model: loaded")
        elif is_llama_model_configured():
            model_error = get_llama_model_error()
            if model_error:
                st.caption(f"llama.cpp model error: {model_error}")
            else:
                st.caption("llama.cpp model: loads on first PDF question")
        else:
            st.caption("llama.cpp model: not configured")

        # Documents Section
        st.subheader("📑 Documents")

        # Get all "document" type sources
        documents = list_sources(chat_id, source_type="document")

        if documents:
            # list the documents
            for doc in documents:
                doc_id = doc[0]
                doc_name = doc[1]
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.write(doc_name)
                with col2:
                    if st.button("❌", key=f"delete_doc_{doc_id}"):
                        if is_pdf_source(doc_name):
                            remove_pdf_sections(chat_id, doc_name)
                        delete_source(doc_id)
                        st.success(f"Deleted document: {doc_name}")
                        st.rerun()
        else:
            st.write("No documents uploaded.")

        uploaded_file = st.file_uploader("Upload Document", key="file_uploader")

        if uploaded_file:
            # Save document content to database
            with st.spinner("Processing document..."):
                temp_dir = "temp_files"
                os.makedirs(temp_dir, exist_ok=True)
                temp_file_path = os.path.join(temp_dir, uploaded_file.name)

                with open(temp_file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                if is_pdf_source(uploaded_file.name):
                    process_pdf_to_sections(temp_file_path, chat_id, uploaded_file.name)
                else:
                    document = load_document(temp_file_path)
                    collection_name = f"chat_{chat_id}"

                    if not os.path.exists("./persist"):
                        create_collection(collection_name, document)
                    else:
                        vectordb = load_collection(collection_name)
                        add_documents_to_collection(vectordb, document)

                # Save source to database
                create_source(uploaded_file.name, "", chat_id, source_type="document")

                # Remove temp file
                os.remove(temp_file_path)
                del st.session_state["file_uploader"]

                st.rerun()

        st.subheader("🔗 Links")

        # Display list of links
        links = list_sources(chat_id, source_type="link")

        if links:
            for link in links:
                link_id = link[0]
                link_url = link[1]
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.markdown(f"[{link_url}]({link_url})")

                with col2:
                    if st.button("❌    ", key=f"delete_link_{link_id}"):
                        delete_source(link_id)
                        st.success(f"Deleted link: {link_url}")
                        st.rerun()
        else:
            st.write("No links added.")

        # Add new link
        new_link = st.text_input("Add a link", key="new_link")
        if st.button("Add Link", key="add_link_btn"):
            if new_link:
                with st.spinner("Processing link..."):
                    # Fetch content from the link
                    try:
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
                        }
                        response = requests.get(new_link, headers=headers)
                        soup = BeautifulSoup(response.text, "html.parser")

                        # Check if the content was successfully retrieved
                        if response.status_code == 200 and soup.text.strip():
                            link_content = soup.get_text(separator="\n")
                        else:
                            st.toast(
                                "Unable to retrieve content from the link. It may be empty or inaccessible.",
                                icon="🚨",
                            )
                            return

                        # Save link content to vector store
                        documents = [
                            Document(
                                page_content=link_content, metadata={"source": new_link}
                            )
                        ]

                        collection_name = f"chat_{chat_id}"

                        if not os.path.exists("./persist"):
                            create_collection(collection_name, documents)
                        else:
                            vectordb = load_collection(collection_name)
                            add_documents_to_collection(vectordb, documents)

                        # Save link to database
                        create_source(new_link, "", chat_id, source_type="link")
                        st.success(f"Added link: {new_link}")
                        del st.session_state["add_link_btn"]
                        st.rerun()
                    except Exception as e:
                        st.toast(
                            f"Failed to fetch content from the link: {e}", icon="⚠️"
                        )
            else:
                st.toast("Please enter a link", icon="❗")


def main():
    """
    Main entry point for the chat application.
    Handles routing between the chats list page and individual chat pages:
    - If a chat_id is present in URL parameters, displays that specific chat
    - Otherwise shows the main chats listing page

    The function uses Streamlit query parameters to maintain state between page loads
    and determine which view to display.
    """

    query_params = st.query_params
    if "chat_id" in query_params:
        chat_id = query_params["chat_id"]
        chat_page(chat_id)
    else:
        chats_home()


if __name__ == "__main__":
    main()
