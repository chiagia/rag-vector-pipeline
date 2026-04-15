from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_core.documents import Document
from typing import List
import os

class DocumentLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load(self) -> List[Document]:
        documents = []

        for root, _, files in os.walk(self.data_path):
            for file in files:
                file_path = os.path.join(root, file)

                if file.endswith("txt"):
                    docs = self._load_txt(file_path)
                    documents.extend(docs)

                elif file.endswith(".pdf"):
                    docs = self._load_pdf(file_path)
                    documents.extend(docs)

        print(f"Loaded {len(documents)} documents")
        return documents
    
    def _load_txt(self, file_path: str) -> List[Document]:
        loader = TextLoader(file_path, encoding="utf-8")
        return loader.load()
    
    def _load_pdf(self, file_path: str) -> List[Document]:
        loader = PyMuPDFLoader(file_path)
        return loader.load()
    
"""
This returns a list, where each element has the structure of a Document

Document(
    page_content="testo del documento...",
    metadata={
        "source": "...",
        "page": 0,
        ...
    }
)
"""