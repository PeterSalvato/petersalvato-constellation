from scripts.semantic_index import SemanticIndexer


def test_detect_aetherwright_mention():
    indexer = SemanticIndexer()
    chat = {
        "title": "Order of the Aetherwright structure",
        "content": "The ritual framework for sovereign cognition...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "order-of-the-aetherwright" in projects
    assert projects["order-of-the-aetherwright"]["confidence"] == "high"


def test_detect_savepoint_keyword():
    indexer = SemanticIndexer()
    chat = {
        "title": "Thinking about turning points",
        "content": "I need to mark where my understanding shifted, like a savepoint in thinking...",
        "timestamp": "2026-01-26T13:04:42.022Z"
    }

    projects = indexer.detect_projects(chat)

    assert "savepoint-protocol" in projects
    assert projects["savepoint-protocol"]["confidence"] == "medium"
