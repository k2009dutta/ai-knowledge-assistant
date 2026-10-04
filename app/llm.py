from ollama import chat
from pydantic import BaseModel
from app.config import LLM_MODEL, LLM_TEMPERATURE
from app.tools import get_cluster_status

SYSTEM_PROMPT = """
You are an AI Knowledge Assistant.
Your responsibilities:
- Explain technical concepts clearly and practically.
- Prefer simple explanations before goin into advanced details.
- Use examples when they improve understanding.
- Explain in less than 10 lines, preferrably under 10 lines.
- If the question is ambiguous, state the assumptions you are making.
"""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_cluster_status",
            "description": "Returns the current status of the Kubernetes cluster.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

class LLMResult(BaseModel):
    answer: str
    model: str
    input_tokens: int
    output_tokens: int

def generate_answer(question: str) -> LLMResult:
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
            ],
            tools=TOOLS,
            options={
                "temperature": LLM_TEMPERATURE
            }
        )
        print(response)
        return response.message.content
        # return LLMResult(
        #     answer=response.message.content,
        #     model=response.model,
        #     input_tokens=response.prompt_eval_count or 0,
        #     output_tokens=response.eval_count or 0
        # )
    
    except Exception as exc:
        raise RuntimeError(
            f"LLM service is unavailable: {exc}"
        )