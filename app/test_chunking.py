# Tests chunking using the actual PDF documents.
# Loads PDFs, splits their text into overlapping chunks, and displays chunk metadata.

from app.pdf_loader import load_pdfs
from app.chunking import chunk_text

documents = load_pdfs("app/documents")

for document in documents:
    chunks = chunk_text(
        text=document["text"],
        source=document["source"],
        chunk_size=500,
        overlap=50
    )
    print("\n***************************")
    print(f"\nSource: {document['source']}")
    print(f"Number of chunks: {len(chunks)}")

    for chunk in chunks:
        print("\n---------------------------")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Source: {chunk['source']}")
        print(f"Text: {chunk['text'][:200]}")
