## Project Overview
A research assistant agent built with LangGraph. It searches DuckDuckGo and Wikipedia **in parallel**, checks whether the results are sufficient, retries automatically if not, and synthesizes a final report using an LLM. Unlike a simple linear pipeline, this project uses a real graph with parallel branches and a conditional self-correction loop.

## Features
- Parallel search across DuckDuckGo and Wikipedia
- Self-correction loop: retries search if results are empty
- Report synthesis using OpenAI (gpt-4o-mini)
- Resilient to individual API failures (if one source fails, the other still works)

## Technologies
- [LangGraph](https://github.com/langchain-ai/langgraph) — graph orchestration
- OpenAI GPT-4o-mini — report synthesis
- [ddgs](https://pypi.org/project/ddgs/) — DuckDuckGo search
- [wikipedia-api](https://pypi.org/project/Wikipedia-API/) — Wikipedia search
- [uv](https://github.com/astral-sh/uv) — Python package manager


## Installation
git clone https://github.com/snz-mlcoder/agent-research-parallel.git
cd agent-research-parallel
uv sync

cp .env.example .env
then add your OPENAI_API_KEY

## Usage
uv run python main.py --query "your research question"

## Project Structure
src/
├── state.py          # Shared state schema
├── graph.py           # LangGraph wiring (parallel + conditional)
└── nodes/
    ├── search_duckduckgo.py
    ├── search_wikipedia.py
    ├── quality_check.py
    └── synthesis.py
main.py                 # CLI entry point


## Known Limitations
- DuckDuckGo rarely returns empty results, even for meaningless queries — so the self-correction loop is hard to trigger in practice with DuckDuckGo alone.
- If `OPENAI_API_KEY` is completely missing (not just invalid), the app crashes on import rather than showing a clean error, since the OpenAI client is initialized at module load time.