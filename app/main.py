from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.0"
)

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    question: str
    answer: str

@app.get("/")
def root():
    return {
        "message": "AI Knowledge Assistant is running."
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    return {
        "question": request.question,
        "answer": "LLM integration will come next."
    }