# Tests the complete RAG flow independently of the FastAPI application.
# Retrieves relevant documents from ChromaDB and generates a grounded LLM response.

from app.rag import generate_rag_answer

questions = [
    "How does Kubernetes recover from a failed container?",
    "How does AWS EKS provide a highly available Kubernetes control plane?",
    "How should Terraform state be migrated?",
    "How should AWS secrets and credentials be secured?"
]

for question in questions:
    print("=" * 80)
    print(f"Question: {question}")

    result = generate_rag_answer(question)

    print("\nRAG answer:")
    print("=" * 80)
    print(result["answer"])

    print("\nSources:")
    print("=" * 80)
    for source in result["sources"]:
        print(f"o {source['source']} (chunk: {source['chunk_id']})")