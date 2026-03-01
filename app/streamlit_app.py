from ui.sidebar import sidebar
from ui.chat_page import chat_page


def main() -> None:
    """Entry point for the Streamlit application."""

    sidebar()
    chat_page()


if __name__ == "__main__":
    main()