from typing import Iterable
from langchain_core.documents import Document


class RAGService:
    """
    Encapsulates retrieval and generation logic for the RAG pipeline.
    """

    def __init__(self, retriever, chain, memory) -> None:
        self.retriever = retriever
        self.chain = chain
        self.memory = memory

    def stream(self, question: str) -> Iterable[str]:
        """
        Streams a response based on retrieved document context.
        """

        # Retrieve relevant documents
        documents: list[Document] = self.retriever.invoke(question)

        if not documents:
            context = ""
        else:
            context = "\n\n".join(
                doc.page_content for doc in documents
            )

        # Stream response from LLM
        return self.chain.stream(
            {
                "context": context,
                "question": question,
                "chat_history": self.memory.buffer_as_messages,
            }
        )