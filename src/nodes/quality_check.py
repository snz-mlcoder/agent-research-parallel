
from src.state import ResearchState


def quality_check(state: ResearchState)-> dict:

    duckduckgo_results = state["duckduckgo_results"]
    wikipedia_results = state["wikipedia_results"]
    retry_count = state["retry_count"]

    if not duckduckgo_results and not wikipedia_results and retry_count < 2:
        return {"needs_retry": True , "retry_count": retry_count + 1}
    else:
        return {"needs_retry": False, "retry_count": retry_count}  