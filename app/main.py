from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.rag import generate_rag_answer

app = FastAPI(
    title="AI Knowledge Assistant",
    version="2.0"
)

class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500
    )

class Source(BaseModel):
    source: str
    chunk_id: str

class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]

@app.get("/")
def root():
    return {
        "message": "AI Knowledge Assistant is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    try:
        result = generate_rag_answer(request.question)
        
        return {
            "question": request.question,
            "answer": result["answer"],
            "sources": result["sources"]
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            details=f"RAG processing failed: {str(e)}"
        )