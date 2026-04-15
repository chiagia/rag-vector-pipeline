from src.ingestion.loader import DocumentLoader
from src.ingestion.chunking import DocumentChunker
from src.embeddings.embedding_manager import EmbeddingManager
from src.vectorstore.chroma_store import ChromaVectorStore

if __name__ == "__main__":

    # Loader 
    loader = DocumentLoader("data/raw")
    documents = loader.load()
    #print(documents[:2])

    # Chuncker
    chunker = DocumentChunker(chunk_size=300, chunk_overlap=50)
    chunks = chunker.split(documents)
    print(f"Number of chunks: {len(chunks)}")
    #print("---Sample chunk---")
    #print(chunks[0].page_content)
    #print(chunks[0].metadata)

    # Embedding
    embedder = EmbeddingManager()
    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedder.embed_texts(texts)

    # Vector store
    vectorstore = ChromaVectorStore()
    vectorstore.add(chunks, embeddings)

    # Query

    query = "Who is Yiruma?"
    query_embedding = embedder.embed_query(query)

    results = vectorstore.collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    print("--- Query results ---")
    for i, doc in enumerate(results["documents"][0]):
        print(f"Result {i+1}:")
        print(doc)
        print()
