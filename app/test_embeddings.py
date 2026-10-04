# Demonstrates text-to-vector embedding generation and cosine similarity.
# Compares a user query with sample documents to show semantic matching.

from app.embeddings import generate_embedding
from app.similarity import cosine_similarity

documents = [
    "Kubernetes automatically restarts unhealthy containers.",
    "Kubernetes recovers failed containers.",
    "Amazon S3 provides object storage."
]

for d in documents:
    vector = generate_embedding(d)
    print(f"Text: {d}")
    print(f"Vector Dimensions: {len(vector)}")
    print(f"First 10 values: {vector[:10]}")

question = "How does Kubernetes recover from a failed container?"

question_vector = generate_embedding(question)

for document in documents:
    document_vector = generate_embedding(document)

    similarity = cosine_similarity(question_vector, document_vector)

    print(f"\nDocument: {document}")
    print(f"Similarity: {similarity:.4f}")