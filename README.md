# 📚 Document Embedding Pipeline

A modular pipeline for document ingestion, processing, and semantic retrieval using embeddings and a vector database.

---

## 🚀 Overview

This project implements a complete pipeline to:

- Load documents from multiple formats (TXT, PDF)
- Split them into smaller semantic chunks
- Generate embeddings using a Transformer-based model
- Store embeddings in a persistent vector database (ChromaDB)
- Perform semantic similarity search over the stored data

---

## 🧠 Pipeline

Documents → Loader → Chunking → Embeddings → Vector Store → Query

---

## 📂 Project Structure

rag-vector-pipeline/
│
├── data/
│ ├── raw/ # Input documents (PDF, TXT)
│ └── vector_store/ # Persistent ChromaDB storage
│
├── src/
│ ├── ingestion/
│ │ ├── loader.py
│ │ └── chunking.py
│ │
│ ├── embeddings/
│ │ └── embedding_manager.py
│ │
│ ├── vectorstore/
│ │ └── chroma_store.py
│
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Features

- Multi-format document loading (TXT, PDF)
- Recursive text chunking with overlap
- Transformer-based embeddings (`SentenceTransformers`)
- Persistent vector storage with ChromaDB
- Semantic search (similarity-based retrieval)

---

## 🛠️ Installation

```bash
git clone <your-repo-url>
cd rag-vector-pipeline

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt

---

## ▶️ Usage

1. Add your documents to: data/raw/

2. Run the pipeline: python main.py

---

## 🔍 Example Query

Query: "Who is Yiruma?"


### Output

- Returns the most semantically relevant text chunks from the documents  
- Each result corresponds to a chunk of the original document  

---

## 🧠 How It Works

- Documents are loaded and converted into structured objects  
- Text is split into overlapping chunks to preserve context  
- Each chunk is converted into a fixed-size embedding vector  
- Embeddings are stored in a vector database  
- Queries are embedded and matched against stored vectors using similarity search  

---

## 📌 Notes

- The system performs **semantic retrieval**, not text generation  
- Results are retrieved chunks, not synthesized answers  
- This pipeline can be extended into a full RAG system by adding an LLM  

