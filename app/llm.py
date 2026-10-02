from ollama import chat

def generate_answer(question: str) -> str:
    response = chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.message.content