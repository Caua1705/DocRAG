import tempfile
from typing import Any

from services.document_loader import (
    load_pdf,
    load_csv,
    load_text_file,
    load_website,
    load_youtube_transcript,
)


def load_document(
    file_type: str,
    file_input: Any,
    api_key: str,
    top_k: int,
):
    """
    Loads a document based on its type and returns a configured retriever.
    """

    if file_type == "Site":
        return load_website(file_input, api_key, top_k)

    if file_type == "Youtube":
        return load_youtube_transcript(file_input, api_key, top_k)

    if file_type in {"Pdf", "Csv", "Txt"}:

        suffix_map = {
            "Pdf": ".pdf",
            "Csv": ".csv",
            "Txt": ".txt",
        }

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix_map[file_type],
        ) as temp_file:
            temp_file.write(file_input.read())
            file_path = temp_file.name

        loader_map = {
            "Pdf": load_pdf,
            "Csv": load_csv,
            "Txt": load_text_file,
        }

        return loader_map[file_type](file_path, api_key, top_k)

    raise ValueError(f"Unsupported file type: {file_type}")