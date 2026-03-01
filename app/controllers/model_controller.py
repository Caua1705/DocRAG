import streamlit as st
from langchain.prompts import ChatPromptTemplate

from core.settings import MODEL_REGISTRY, create_memory
from core.prompts import build_system_prompt
from controllers.document_controller import load_document
from services.rag_service import RAGService


def initialize_model(
    provider: str,
    model_name: str,
    api_key: str,
    embedding_api_key: str,
    file_type: str,
    file_input,
    top_k: int,
) -> None:
    """
    Initializes the RAG pipeline and stores the service in session state.
    """

    if not api_key:
        raise ValueError("LLM API key is required.")

    if not embedding_api_key:
        raise ValueError("Embedding API key is required.")

    # Create retriever
    retriever = load_document(
        file_type=file_type,
        file_input=file_input,
        api_key=embedding_api_key,
        top_k=top_k,
    )

    # Create LLM
    provider_config = MODEL_REGISTRY[provider]
    chat_class = provider_config["chat_class"]

    llm = chat_class(
        model=model_name,
        api_key=api_key,
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", build_system_prompt()),
            ("placeholder", "{chat_history}"),
            ("human", "{question}"),
        ]
    )

    chain = prompt | llm

    # Create memory
    memory = create_memory()

    # Create RAG service
    rag_service = RAGService(
        retriever=retriever,
        chain=chain,
        memory=memory,
    )

    # Store only the service
    st.session_state["rag_service"] = rag_service