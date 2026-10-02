# AI Knowledge Assistant

A production-oriented AI Knowledge Assistant built using modern LLM, RAG, agentic AI, cloud, Kubernetes, and DevOps technologies.

The project starts with a local LLM-based application and progressively evolves into a cloud-native AI platform running on AWS and Kubernetes.

---

## Project Goal

Build an AI Knowledge Assistant that can:

- Answer questions using an LLM
- Maintain conversational context
- Ingest and process documents
- Search a knowledge base using semantic search
- Generate grounded answers using Retrieval-Augmented Generation (RAG)
- Provide source references for answers
- Use tools through an AI agent
- Support local LLMs during development
- Integrate with managed foundation models on AWS
- Run as a containerized, production-oriented application on Amazon EKS

---

# Current Architecture

```text
                    User
                      |
                      v
                  FastAPI
                      |
                      v
                Pydantic
                 Validation
                      |
                      v
                LLM Service
                   llm.py
                      |
          +-----------+-----------+
          |                       |
    System Prompt            Configuration
          |                       |
          +-----------+-----------+
                      |
                      v
                   Ollama
                      |
                      v
                  Gemma LLM
                      |
                      v
                AI Response