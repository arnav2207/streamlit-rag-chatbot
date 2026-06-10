import streamlit as st
import os, time, math
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



def main():
       chats_home()

if __name__ == "__main__":
    main()

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
        # Load retriever for the chat context
        collection_name = f"chat_{chat_id}"
        if os.path.exists(f"./persist"):
            retriever = load_retriever(collection_name=collection_name)
        else:
            retriever = None

        # Ask question using the retriever
        response = (
            generate_answer_from_context(retriever, prompt)
            if retriever
            else "I need some context to answer that question."
        )

        # Save AI response
        create_message(chat_id, "ai", response)
    
        # Display AI response
        with st.chat_message("assistant"):
            st.write_stream(stream_response(response))

        st.rerun()