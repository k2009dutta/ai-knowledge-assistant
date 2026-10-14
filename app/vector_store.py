# Provides the vector-store layer for storing document chunks,
# embeddings, metadata, and performing semantic search with ChromaDB.

import chromadb
from app.embeddings import generate_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)

def add_chunk(chunk_id: str, text: str, source: str):
    embedding = generate_embedding(text)

    collection.add(
        ids=[chunk_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "source": source,
                "chunk_id": chunk_id
            }
        ]
    )

def search_documents(query: str, top_k: int = 3):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results