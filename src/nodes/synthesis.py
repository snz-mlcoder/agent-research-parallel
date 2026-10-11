

from dotenv import load_dotenv

from src.state import ResearchState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, max_tokens=250, request_timeout=120)

def synthesis(state: ResearchState):
    duckduckgo_results = state["duckduckgo_results"]
    wikipedia_results = state["wikipedia_results"]
    query = state["query"]

    if not duckduckgo_results and not wikipedia_results:
        return {"report": f"No information could be found for '{query}' after multiple search attempts."}
    
    prompt = PromptTemplate(
        input_variables=["duckduckgo_results", "wikipedia_results", "query"],
        template="You are a research assistant. Using ONLY the information provided below, "
        "write a concise report (max 150 words) on '{query}'. "
        "Do not add information beyond what is given.\n\n"
        "DuckDuckGo Results:\n{duckduckgo_results}\n\n"
        "Wikipedia Results:\n{wikipedia_results}"
    )
    filled_prompt = prompt.format(
        duckduckgo_results=duckduckgo_results,
        wikipedia_results=wikipedia_results,
        query=query
    )
    try:
        response = llm.invoke(filled_prompt)
        return {"report": response.content}
    except Exception as e:
        print(f"Error occurred while synthesizing report: {e}")
        return {"report": "Error occurred while synthesizing report."}
