# Provides the vector-store layer for storing document embeddings and
# performing semantic search with ChromaDB.

import chromadb
from app.embeddings import generate_embedding

client = chromadb.PersistentClient(
    path="./chrome_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)

def add_document(document_id: str, text: str):
    embedding = generate_embedding(text)

    collection.add(
        ids=[document_id],
        documents=[text],
        embeddings=[embedding]
    )

def search_documents(query: str, top_k: int = 2):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results