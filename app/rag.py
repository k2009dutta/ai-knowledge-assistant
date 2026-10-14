# Implements the Retrieval-Augmented Generation pipeline.
# Retrieves relevant documents from ChromaDB and uses them as context for the LLM.

from app.vector_store import search_documents
from app.llm import generate_answer

def generate_rag_answer(question: str):
    results = search_documents(question, top_k=3)
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    if not documents:
      return {
        "answer": "No relevant information was found in the knowledge base.",
        "sources": []
      }
    
    context_parts = []
    sources = []

    for index, document in enumerate(documents):
      metadata = metadatas[index]
      context_parts.append(document)

      sources.append({
        "source": metadata["source"],
        "chunk_id": metadata["chunk_id"]
      })

    context = "\n\n".join(context_parts)

    prompt = f"""
    You are answering a question using a knowledge base.
    Use the context below as the primary source of truth.

    Context:
    {context}

    Question:
    {question}

    Instructions:
    - Answer the question only using the provided context.
    - Do no introduce facts that are not present in the context.
    - If the context does not contain enough information to answer the question, say so.
    - Keep the answer concise and clear.
    """

    answer = generate_answer(prompt)
    
    #Remove duplicate source entries while preservind their order
    unique_sources = list({
      (source["source"], source["chunk_id"]): source
      for source in sources
    }.values())

    return {
      "answer": answer,
      "sources": unique_sources
    }