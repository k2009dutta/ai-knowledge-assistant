from fastapi import FastAPI
from pydantic import BaseModel
from app.llm import generate_answer

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.1"
)

class AskRequest(BaseModel):
    question: str

class Usage(BaseModel):
    input_tokens: int
    output_tokens: int

class AskResponse(BaseModel):
    question: str
    answer: str
    model: str
    usage: Usage

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
    result = generate_answer(request.question)
    
    return {
        "question": request.question,
        "answer": result.answer,
        "model": result.model,
        "usage": {
            "input_tokens": result.input_tokens,
            "output_tokens": result.output_tokens
        }
    }