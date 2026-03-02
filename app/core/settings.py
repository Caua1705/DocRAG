from enum import Enum
from typing import Dict, Type

from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


class FileType(str, Enum):
    """Supported document types."""

    SITE = "Site"
    YOUTUBE = "Youtube"
    PDF = "Pdf"
    CSV = "Csv"
    TXT = "Txt"


class Provider(str, Enum):
    """Supported LLM providers."""

    OPENAI = "OpenAI"
    GROQ = "Groq"


MODEL_REGISTRY: Dict[Provider, Dict[str, object]] = {
    Provider.GROQ: {
        "models": [
            "llama-3.1-70b-versatile",
            "gemma2-9b-it",
            "mixtral-8x7b-32768",
        ],
        "chat_class": ChatGroq,
    },
    Provider.OPENAI: {
        "models": [
            "gpt-4o-mini",
            "gpt-4o",
            "o1-preview",
            "o1-mini",
        ],
        "chat_class": ChatOpenAI,
    },
}


def create_memory() -> ConversationBufferMemory:
    """Factory function for conversation memory."""
    return ConversationBufferMemory()