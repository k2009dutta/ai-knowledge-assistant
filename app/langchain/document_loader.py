from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

DOCUMENTS_DIR = Path(__file__).resolve().parents[1] / "documents"

def load_pdfs():
    documents = []

    for pdf in DOCUMENTS_DIR.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    return documents