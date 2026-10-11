from dotenv import load_dotenv
from src.graph import graph

load_dotenv()

def main():
    query = "Python programming"
    initial_state = {
        "query": query,
        "duckduckgo_results": [],
        "wikipedia_results": [],
        "needs_retry": False,
        "retry_count": 0,
        "report": "",
    }
    result = graph.invoke(initial_state)
    print(f"DuckDuckGo results: {len(result['duckduckgo_results'])}")
    print(f"Wikipedia results: {len(result['wikipedia_results'])}")
    print(f"\nReport:\n{result['report']}")

if __name__ == "__main__":
    main()