from fastapi import FastAPI
from pydantic import BaseModel
from app.llm import generate_answer

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.1"
)

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    question: str
    answer: str

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
    answer = generate_answer(request.question)
    
    return {
        "question": request.question,
        "answer": answer
    }