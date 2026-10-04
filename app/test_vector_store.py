from app.vector_store import add_document, search_documents

documents = [
    (
        "doc1", "Kubernetes automatically restarts unhealthy containers."
    ),
    (
        "doc2", "Kubernetes recovers failed containers."
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