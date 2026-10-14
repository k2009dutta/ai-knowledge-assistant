# Tests PDF ingestion by loading all PDFs from the documents directory
# and displaying their filenames and extracted text.

from app.pdf_loader import load_pdfs

documents = load_pdfs("app/documents")

print(f"\nFound {len(documents)} PDF Files...")

for document in documents:
    print("\n=============================")
    print(f"Source: {document['source']}")
    print("==============================")
    print(document["text"][:500])
