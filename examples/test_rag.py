import sys
from src.retrieval.rag_index import LocalRepositoryRAG

def test_retrieval(query: str):
    rag = LocalRepositoryRAG()
    results = rag.retrieve_context(query)
    
    print(f"--- Retrieval Results for: '{query}' ---")
    for i, res in enumerate(results):
        print(f"\n[Match {i+1}]:\n{res}")

if __name__ == "__main__":
    test_retrieval(sys.argv[1] if len(sys.argv) > 1 else "How is RiskTier defined?")
