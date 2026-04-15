import chromadb
from chromadb.config import Settings
import os
import uuid
from typing import List
import numpy as np
from langchain_core.documents import Document

class ChromaVectorStore:
    def __init__(self, persist_directory: str = "data/vector_store"):
        self.persist_directory = persist_directory
        self.client = None
        self.collection = None
        self._initialize()

    def _initialize(self):
        os.makedirs(self.persist_directory, exist_ok=True)
        self.client = chromadb.PersistentClient(path=self.persist_directory)
        self.collection = self.client.get_or_create_collection(name="document_collection")
        print("ChromaDB initialized")

    def add(self, documents: List[Document], embeddings: np.ndarray):
        if len(documents) != len(embeddings):
            raise ValueError("Documents and embeddings must have the same length")
        
        ids = []
        texts = []
        metadatas = []
        embeddings_list = []

        for i, (doc, emb) in enumerate(zip(documents, embeddings)):
            doc_id = f"doc_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(doc_id)

            texts.append(doc.page_content)
            metadatas.append(doc.metadata)
            embeddings_list.append(emb.tolist())

        self.collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas,
            embeddings=embeddings_list
        )
        print(f"Addes {len(documents)} documents to ChromaDB")


"""
This creates the vector database. 
For each chunk it considers: id, text, metadata and embedding
"""