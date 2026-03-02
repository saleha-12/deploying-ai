from chromadb import PersistentClient

client = PersistentClient(path="./embeddings")
collection = client.get_or_create_collection(name="ai_report")

def semantic_query(query: str):
    """
    Search for semantic matches inside the AI Report 2025 dataset.
    """
    results = collection.query(query_texts=[query], n_results=3)

    docs = results["documents"][0]
    if not docs:
        return "I couldn't find relevant information in the AI Report."

    return "\n\n".join(docs)
