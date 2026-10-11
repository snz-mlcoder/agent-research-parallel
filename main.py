
import argparse

from dotenv import load_dotenv
from src.graph import graph
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Research Assistant")
    parser.add_argument("--query", type=str, default="Python programming", help="Research query")
    args = parser.parse_args()
    query = args.query
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