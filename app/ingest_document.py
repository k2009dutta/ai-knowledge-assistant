# Ingests PDF documents into ChromaDB.
# Extracts text, creates chunks, generates embeddings, and stores metadata.

from app.pdf_loader import load_pdfs
from app.chunking import chunk_text
from app.vector_store import add_chunk

DOCUMENT_DIRECTORY = "app/documents"

documents = load_pdfs(DOCUMENT_DIRECTORY)
total_chunk = 0

for document in documents:
    chunks = chunk_text(
        text=document["text"],
        source=document["source"],
        chunk_size=500,
        overlap=50
    )

    print(
        f"\nProcessing {document['source']}: "
        f"{len(chunks)} chunks"
    )

    for chunk in chunks:
        add_chunk(
            chunk_id=chunk['chunk_id'],
            text=chunk['text'],
            source=chunk['source']
        )
        total_chunk += 1
    
print(
    f"\nIngestion complete... "
    f"Added {total_chunk} chunks to ChromaDB."
)