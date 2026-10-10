from langgraph.graph import StateGraph, START, END
from src.state import ResearchState
from src.nodes.search_duckduckgo import search_duckduckgo
from src.nodes.search_wikipedia import search_wikipedia

graph_builder = StateGraph(ResearchState)

graph_builder.add_node("search_duckduckgo", search_duckduckgo)
graph_builder.add_node("search_wikipedia", search_wikipedia)

graph_builder.add_edge(START, "search_duckduckgo")
graph_builder.add_edge(START, "search_wikipedia")
graph_builder.add_edge("search_duckduckgo", END)
graph_builder.add_edge("search_wikipedia", END)

graph = graph_builder.compile()
