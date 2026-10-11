
from src.state import ResearchState
from ddgs import DDGS

def search_duckduckgo(state: ResearchState):
    query = state["query"]
    try:
        results = DDGS().text(query, max_results=5)
        return {"duckduckgo_results": results}
    except Exception as e:
        print(f"Error occurred while searching DuckDuckGo: {e}")
        return {"duckduckgo_results": []}

    
