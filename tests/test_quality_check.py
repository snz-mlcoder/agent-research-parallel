
from src.nodes.quality_check import quality_check

def test_quality_check_retries_when_both_empty():
    result = quality_check({
        "duckduckgo_results": [],
        "wikipedia_results": [],
        "retry_count": 0
    })
    assert result == {"needs_retry": True, "retry_count": 1}

def test_quality_check_no_retry_when_results_exist():
    result = quality_check({
        "duckduckgo_results": [{"title": "test"}],
        "wikipedia_results": [],
        "retry_count": 0
    })
    assert result == {"needs_retry": False, "retry_count": 0}

def test_quality_check_no_retry_when_retry_count_exceeds():
    result = quality_check({
        "duckduckgo_results": [],
        "wikipedia_results": [],
        "retry_count": 2
    })
    assert result == {"needs_retry": False, "retry_count": 2}
    