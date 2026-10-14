# Tests semantic retrieval against the PDF chunks stored in ChromaDB.
from app.vector_store import search_documents

query = "How does Kubernetes recover from a failed container?"

results = search_documents(query, top_k=3)

print("\nRetrieved chunks:")

for index, document in enumerate(results['documents'][0]):
    metadata = results['metadatas'][0][index]

    print("\n------------------------------------")
    print(f"Source: {metadata['source']}")
    print(f"Chunk ID: {metadata['chunk_id']}")
    print(f"Text: {document}")
