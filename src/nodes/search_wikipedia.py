

from src.state import ResearchState
import wikipediaapi

def search_wikipedia(state: ResearchState):
    query = state["query"]
    try:   
        wiki = wikipediaapi.Wikipedia(user_agent='ResearchAgent/1.0', language='en')
        page = wiki.page(query)
        if page.exists():
            return {"wikipedia_results": [{"title": page.title, "summary": page.summary}]}
        else:
            return {"wikipedia_results": []}
    
    except Exception as e:
        print(f"Error occurred while searching Wikipedia: {e}")
        return {"wikipedia_results": []}
