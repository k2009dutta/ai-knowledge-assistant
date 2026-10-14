# Splits extracted documents into smaller overlapping chunks for RAG retrieval.
# Each chunk retains its source document and a unique chunk ID.

def chunk_text(text: str, source: str, chunk_size: int = 500, overlap: int = 50):
    chunks = []
    start = 0
    chunk_number = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append({
                "chunk_id": f"{source}_{chunk_number}",
                "source": source,
                "text": chunk
            })
        
        chunk_number += 1
        start += chunk_size - overlap
    
    return chunks