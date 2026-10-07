from typing import  TypedDict

class ResearchState(TypedDict):
    """A dictionary representing the state of a research project"""
    query: str
    duckduckgo_results: list[dict]
    wikipedia_results: list[dict]
    needs_retry: bool
    retry_count: int
    report: str