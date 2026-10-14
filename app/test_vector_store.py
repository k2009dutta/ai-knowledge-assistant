# Demonstrates semantic retrieval using ChromaDB.
# Stores sample documents, embeds the query, and retrieves the top-K relevant documents.

from app.vector_store import add_document, search_documents

documents = [
    (
        "doc1",
        "Kubernetes automatically restarts unhealthy containers"
        "when their health checks fail."
    ),
    (
        "doc2",
        "Kubernetes recovers failed containers."
        "When a container or pod fails, Kubernetes replaces it to restore"
        "the desired state"
    ),
    (
        "doc3", "Amazon S3 provides object storage."
    )
]

for document_id, text in documents:
    add_document(document_id, text)

query = "How does Kubernetes recover from a failed container?"

results = search_documents(query, top_k=2)

print("\nRetrieved Documents are:")

for result in results["documents"][0]:
    print("-",result)