# Extracts text from PDF files for the RAG ingestion pipeline.

from pathlib import Path
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    
    return "\n".join(text)

def load_pdfs(directory: str):
    documents = []

    for pdf_path in Path(directory).glob("*.pdf"):
        text = extract_text_from_pdf(str(pdf_path))

        documents.append({
            "source": pdf_path.name,
            "text": text
        })

    return documents