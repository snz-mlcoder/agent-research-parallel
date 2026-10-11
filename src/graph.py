from langgraph.graph import StateGraph, START, END
from src.state import ResearchState
from src.nodes.search_duckduckgo import search_duckduckgo
from src.nodes.search_wikipedia import search_wikipedia
from src.nodes.quality_check import quality_check


def route_after_quality_check(state: ResearchState):
    if state["needs_retry"]:
        return "search_duckduckgo"
    return END

graph_builder = StateGraph(ResearchState)

graph_builder.add_node("search_duckduckgo", search_duckduckgo)
graph_builder.add_node("search_wikipedia", search_wikipedia)
graph_builder.add_node("quality_check", quality_check)
graph_builder.add_edge(START, "search_duckduckgo")
graph_builder.add_edge(START, "search_wikipedia")
graph_builder.add_edge("search_duckduckgo", "quality_check")
graph_builder.add_edge("search_wikipedia", "quality_check")
graph_builder.add_conditional_edges("quality_check", route_after_quality_check)

graph = graph_builder.compile()
