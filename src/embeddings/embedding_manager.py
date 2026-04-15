from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class EmbeddingManager:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"): # dim 384
        self.model_name = model_name
        self.model = self._load_model()

    def _load_model(self):
        print(f"Loading embedding model: {self.model_name}")
        model = SentenceTransformer(self.model_name)
        print("Model loaded!")
        return model
    
    def embed_texts(self, texts: List[str]) -> np.ndarray: # Input: list of chunks; output: matrix (Num chunks, 384)
        print(f"Generating embedding for {len(texts)} texts...")
        embeddings = self.model.encode(texts, show_progress_bar=False)
        print(f"Embedding shape: {embeddings.shape}")
        return embeddings
    
    def embed_query(self, query: str) -> np.ndarray:
        return self.model.encode([query])[0]