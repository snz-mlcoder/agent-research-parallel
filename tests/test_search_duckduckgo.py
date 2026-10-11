from unittest.mock import patch
from src.nodes.search_duckduckgo import search_duckduckgo

@patch('src.nodes.search_duckduckgo.DDGS')
def test_search_duckduckgo_returns_results(mock_ddgs_class):
    # Mock the DDGS instance and its text method
    mock_ddgs_instance = mock_ddgs_class.return_value
    mock_ddgs_instance.text.return_value = [
        {"title": "Result 1", "url": "http://example.com/1"},
        {"title": "Result 2", "url": "http://example.com/2"},
    ]

    state = {
        "query": "test query",
        "duckduckgo_results": [],
        "wikipedia_results": [],
        "needs_retry": False,
        "retry_count": 0,
        "report": "",
    }

    result = search_duckduckgo(state)

    assert result == {
        "duckduckgo_results": [
            {"title": "Result 1", "url": "http://example.com/1"},
            {"title": "Result 2", "url": "http://example.com/2"},
        ]
    }

@patch('src.nodes.search_duckduckgo.DDGS')
def test_search_duckduckgo_handles_exception(mock_ddgs_class):
    # Patch the DDGS class to raise an exception
    mock_ddgs_instance = mock_ddgs_class.return_value
    mock_ddgs_instance.text.side_effect = Exception("Test exception")

    state = {
        "query": "test query",
        "duckduckgo_results": [],
        "wikipedia_results": [],
        "needs_retry": False,
        "retry_count": 0,
        "report": "",
    }

    result = search_duckduckgo(state)

    assert result == {"duckduckgo_results": []}