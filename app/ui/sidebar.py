import streamlit as st

from core.settings import MODEL_REGISTRY, Provider, create_memory
from controllers.model_controller import initialize_model


def sidebar() -> None:
    """Renders the configuration sidebar."""

    with st.sidebar:

        st.title("Configuration")

        # File Type
        file_type = st.selectbox(
            "File type",
            ["Site", "Youtube", "Pdf", "Csv", "Txt"],
        )

        if file_type in {"Site", "Youtube"}:
            file_input = st.text_input("Enter URL or video ID")
        else:
            file_input = st.file_uploader("Upload file")

        # LLM Provider
        provider_value = st.selectbox(
            "LLM Provider",
            [p.value for p in Provider],
        )
        provider = Provider(provider_value)

        # Model
        model_name = st.selectbox(
            "Model",
            MODEL_REGISTRY[provider]["models"],
        )

        # Advanced Retrieval Settings
        with st.expander("Advanced Retrieval Settings"):
            top_k = st.slider(
                "Context Depth",
                min_value=1,
                max_value=10,
                value=3,
                help=(
                    "Controls how many document sections are used to answer your question. "
                    "Lower values = more precise. "
                    "Higher values = more comprehensive but may introduce noise."
                ),
            )

        # API Keys
        llm_api_key = st.text_input(
            "LLM API Key",
            type="password",
        )

        if provider == Provider.GROQ:
            st.warning("Groq does not support embeddings.")
            embedding_api_key = st.text_input(
                "OpenAI API Key (for embeddings)",
                type="password",
            )
        else:
            embedding_api_key = llm_api_key

        # Initialize
        if st.button("Initialize"):

            if not file_input:
                st.error("Please provide a document.")
                return

            if not llm_api_key:
                st.error("LLM API key is required.")
                return

            if provider == Provider.GROQ and not embedding_api_key:
                st.error("OpenAI API key is required for embeddings.")
                return

            try:
                initialize_model(
                    provider=provider,
                    model_name=model_name,
                    api_key=llm_api_key,
                    embedding_api_key=embedding_api_key,
                    file_type=file_type,
                    file_input=file_input,
                    top_k=top_k,
                )

                st.success("Model initialized successfully.")

            except Exception as exc:
                st.error(str(exc))

        # Clear Chat History
        if "rag_service" in st.session_state:
            if st.button("Clear Chat History"):
                rag_service = st.session_state["rag_service"]
                rag_service.memory = create_memory()
                st.success("Chat history cleared.")