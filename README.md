# 📚 DocRAG – Retrieval-Augmented Conversational AI System

## 🌐 Live Demo

🔗 [DocRAG Application](https://docrag-ai.streamlit.app)

---

DocRAG is a modular Retrieval-Augmented Generation (RAG) system designed for scalable and efficient question-answering over unstructured data sources.

Instead of injecting entire documents into a prompt (which is inefficient and non-scalable), DocRAG implements semantic search using embeddings and a FAISS vector database to retrieve only the most relevant chunks before passing structured context to a Large Language Model (LLM).

The system follows a modular backend architecture with clear separation of concerns between UI, application logic, and retrieval logic.

---

## 🚀 Core Features

- Multi-source document ingestion:
  - PDF files
  - CSV files
  - Text files
  - Website scraping (URL-based)
  - YouTube transcript extraction
- Retrieval-Augmented Generation (RAG)
- Recursive text chunking with overlap
- Embeddings-based semantic retrieval
- FAISS vector store integration
- OpenAI and Groq LLM provider support
- Encapsulated RAG service layer
- API key validation before initialization
- Modular and extensible project structure

---

## 🧠 System Architecture


app/
├── ui/ # Streamlit interface
├── controllers/ # Application orchestration layer
├── services/ # RAG and document services
├── core/ # Configuration, providers, prompts
└── streamlit_app.py


### Layer Responsibilities

**UI Layer**
- Handles user interaction
- Displays chat history
- Delegates logic to service layer

**Controller Layer**
- Initializes retriever and LLM
- Builds prompt template
- Instantiates RAG service
- Manages session state

**Service Layer**
- Encapsulates RAG pipeline
- Handles retrieval
- Builds contextual prompt
- Manages conversation memory

---

## 🔎 Retrieval Pipeline

1. Document ingestion  
2. Recursive text chunking  
3. Embedding generation  
4. Vector indexing (FAISS)  
5. Top-k semantic retrieval  
6. Context-aware LLM generation  

This architecture improves:

- Scalability
- Context precision
- Token efficiency
- Cost optimization

---

## ⚙️ Technologies

- Python 3.11
- Streamlit
- LangChain
- OpenAI API
- Groq API
- FAISS (Vector Similarity Search)
- RecursiveCharacterTextSplitter

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/docrag.git
cd docrag
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

From the project root directory:

```bash
streamlit run app/streamlit_app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 🔐 API Key Configuration

Before initializing the model, you must provide a valid API key in the sidebar.

- OpenAI models require an OpenAI API key.
- Groq models require a Groq API key.
- Embeddings are generated using OpenAI embeddings.

The application validates required keys before starting a session.

---

## 📌 Engineering Decisions

- Clear separation between UI and business logic
- Encapsulation of the RAG pipeline inside a dedicated service layer
- Provider registry pattern for model extensibility
- Context-controlled system prompt
- Top-k semantic retrieval strategy

---

## 🚧 Planned Improvements

- Persistent vector storage
- Vector index versioning
- Automated evaluation pipeline
- Multi-document indexing
- Advanced retrieval strategies (hybrid search, re-ranking)
- Structured logging
- Docker containerization
- Cloud deployment automation

---

## 🎯 Project Objective

DocRAG demonstrates:

- Practical implementation of Retrieval-Augmented Generation
- Modular backend architecture
- Integration between LLMs and vector databases
- Applied AI engineering principles for document-based systems

Developed as a technical portfolio project targeting AI Engineering, Applied Data, and Backend Python roles.

---

## 👨‍💻 Author

Portfolio project developed for internship applications in AI, Data, and Backend development.