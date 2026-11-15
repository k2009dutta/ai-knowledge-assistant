from app.langchain.llm import llm

response = llm.invoke(
    "Explain Kubernetes in one sentence."
)

print(response.content)