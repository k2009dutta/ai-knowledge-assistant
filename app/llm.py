from ollama import chat
from app.config import LLM_MODEL

SYSTEM_PROMPT = (
    "You are an AI Knowledge Assistant."
    "Explain technical concepts clearly and practically."
    "Explain in less than 10 lines, if possible"
    "Use examples when possible."
)

def generate_answer(question: str) -> str:
    try:
        response = chat(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response.message.content
    
    except Exception as exc:
        raise RuntimeError(
            f"LLM service is unvailable: {exc}"
        )