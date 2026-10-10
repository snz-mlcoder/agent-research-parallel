
from src.state import ResearchState
from ddgs import DDGS

def search_duckduckgo(state: ResearchState):
    query = state["query"]
    results = DDGS().text(query, max_results=5)
    
    return {"duckduckgo_results": results}
