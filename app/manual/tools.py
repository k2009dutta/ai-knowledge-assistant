# Defines application tools that an LLM can invoke to
# access external or application-specific information.

def get_cluster_status() -> dict:
    return {
        "cluster": "ai-demo-cluster",
        "status": "healthy",
        "nodes": 3,
        "version": "1.35"
    }