from typing import List

from langchain_community.document_loaders import (
    WebBaseLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document


def split_documents(documents: List[Document]) -> List[Document]:
    """
    Splits documents into smaller overlapping chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )
    return splitter.split_documents(documents)


def build_vector_store(
    documents: List[Document],
    api_key: str,
) -> FAISS:
    """
    Creates a FAISS vector store from document chunks.
    """
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=api_key,
    )

    return FAISS.from_documents(
        documents=documents,
        embedding=embedding_model,
    )


def build_retriever_from_documents(
    documents: List[Document],
    api_key: str,
    top_k: int,
):
    """
    Builds a retriever with configurable top_k.
    """
    splits = split_documents(documents)
    vector_store = build_vector_store(splits, api_key)

    return vector_store.as_retriever(
        search_kwargs={"k": top_k}
    )


def load_pdf(path: str, api_key: str, top_k: int):
    loader = PyPDFLoader(path)
    documents = loader.load()
    return build_retriever_from_documents(documents, api_key, top_k)


def load_csv(path: str, api_key: str, top_k: int):
    loader = CSVLoader(path)
    documents = loader.load()
    return build_retriever_from_documents(documents, api_key, top_k)


def load_text_file(path: str, api_key: str, top_k: int):
    loader = TextLoader(path)
    documents = loader.load()
    return build_retriever_from_documents(documents, api_key, top_k)


def load_website(url: str, api_key: str, top_k: int):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return build_retriever_from_documents(documents, api_key, top_k)


def load_youtube_transcript(video_id: str, api_key: str, top_k: int):
    from youtube_transcript_api import YouTubeTranscriptApi

    transcript = YouTubeTranscriptApi.get_transcript(
        video_id,
        languages=["pt"],
    )

    text = " ".join(chunk["text"] for chunk in transcript)

    documents = [Document(page_content=text)]

    return build_retriever_from_documents(documents, api_key, top_k)