import streamlit as st


def chat_page() -> None:
    """
    Renders the chat interface and handles user interaction.
    """

    st.header("🤖 DocRAG", divider=True)

    rag_service = st.session_state.get("rag_service")

    if rag_service is None:
        st.warning("Please initialize the model first.")
        return

    memory = rag_service.memory

    # Display chat history
    for message in memory.buffer_as_messages:
        with st.chat_message(message.type):
            st.markdown(message.content)

    user_input = st.chat_input("Ask a question about the document")

    if not user_input:
        return

    # Display user message
    with st.chat_message("human"):
        st.markdown(user_input)

    # Stream assistant response
    with st.chat_message("ai"):
        response = st.write_stream(
            rag_service.stream(user_input)
        )

    # Persist conversation in memory
    if response:
        memory.chat_memory.add_user_message(user_input)
        memory.chat_memory.add_ai_message(response)