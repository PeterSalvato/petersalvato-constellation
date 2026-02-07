# tests/test_chat_ingest.py
import json
from scripts.chat_ingest import GeminiParser, ChatGPTParser, ChatExportLoader

def test_gemini_parser_extracts_title():
    sample_gemini = {
        "title": "Prompted test subject",
        "time": "2026-01-26T13:04:42.022Z",
        "safeHtmlItem": [{"html": "<p>Test content</p>"}]
    }

    parser = GeminiParser()
    result = parser.parse_chat(sample_gemini)

    assert result["title"] == "Prompted test subject"
    assert result["timestamp"] == "2026-01-26T13:04:42.022Z"
    assert "<p>" not in result["content"]  # HTML stripped
    assert "Test content" in result["content"]

def test_gemini_parser_handles_missing_html():
    sample_gemini = {
        "title": "Test",
        "time": "2026-01-26T13:04:42.022Z",
        "safeHtmlItem": []
    }

    parser = GeminiParser()
    result = parser.parse_chat(sample_gemini)

    assert result["content"] == ""

def test_load_gemini_export():
    loader = ChatExportLoader()
    chats = loader.load_gemini(
        "/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json"
    )

    assert isinstance(chats, list)
    assert len(chats) > 0
    assert all("timestamp" in c for c in chats)
    assert all(c["platform"] == "gemini" for c in chats)

def test_chatgpt_parser_extracts_title():
    sample_chatgpt = {
        "name": "AI Persona Management Strategies",
        "created_at": "2025-09-08T16:14:33.766919Z",
        "chat_messages": [
            {
                "sender": "human",
                "created_at": "2025-09-08T16:14:34.320224Z",
                "text": "How do I set up personas?",
                "content": [{"type": "text", "text": "How do I set up personas?"}]
            },
            {
                "sender": "assistant",
                "created_at": "2025-09-08T16:14:40.000000Z",
                "text": "Here are the steps...",
                "content": [{"type": "text", "text": "Here are the steps..."}]
            }
        ]
    }

    parser = ChatGPTParser()
    result = parser.parse_conversation(sample_chatgpt)

    assert result["title"] == "AI Persona Management Strategies"
    assert result["timestamp"] == "2025-09-08T16:14:33.766919Z"
    assert result["platform"] == "chatgpt"
    assert "human: How do I set up personas?" in result["content"]
    assert "assistant: Here are the steps..." in result["content"]

def test_chatgpt_parser_extracts_content_from_content_array():
    """Test that content is extracted from content array when text field is empty"""
    sample_chatgpt = {
        "name": "Test conversation",
        "created_at": "2025-09-08T16:14:33.766919Z",
        "chat_messages": [
            {
                "sender": "human",
                "text": "",  # Empty text field
                "content": [{"type": "text", "text": "Question from content array"}]
            },
            {
                "sender": "assistant",
                "text": "Response",
                "content": [{"type": "text", "text": "Should be ignored"}]
            }
        ]
    }

    parser = ChatGPTParser()
    result = parser.parse_conversation(sample_chatgpt)

    assert "human: Question from content array" in result["content"]
    assert "assistant: Response" in result["content"]

def test_chatgpt_parser_filters_empty_messages():
    """Test that completely empty messages are filtered out"""
    sample_chatgpt = {
        "name": "Test",
        "created_at": "2025-09-08T16:14:33.766919Z",
        "chat_messages": [
            {
                "sender": "human",
                "text": "",
                "content": [{"type": "text", "text": ""}]
            },
            {
                "sender": "assistant",
                "text": "Real content",
                "content": [{"type": "text", "text": "Real content"}]
            }
        ]
    }

    parser = ChatGPTParser()
    result = parser.parse_conversation(sample_chatgpt)

    # Should not have the empty message, only the assistant's
    assert "human:" not in result["content"]
    assert "assistant: Real content" in result["content"]

def test_load_chatgpt_export():
    loader = ChatExportLoader()
    chats = loader.load_chatgpt(
        "/home/peter/homelab/knowledge/exports/data-2026-01-26-15-50-54-batch-0000/conversations.json"
    )

    assert isinstance(chats, list)
    assert len(chats) > 0
    assert all("timestamp" in c for c in chats)
    assert all("content" in c for c in chats)
    assert all("title" in c for c in chats)
    assert all(c["platform"] == "chatgpt" for c in chats)

def test_end_to_end_extraction():
    """Load all chats, index them, build timelines, extract for Aetherwright"""
    from scripts.chat_ingest import ChatExportLoader
    from scripts.semantic_index import SemanticIndexer
    from scripts.lineage_builder import LineageBuilder

    # Load
    loader = ChatExportLoader()
    chats = loader.load_gemini(
        "/home/peter/homelab/knowledge/exports/takeout-20260126T155729Z-3-001/Takeout/My Activity/Gemini Apps/MyActivity.json"
    )

    # Index
    indexer = SemanticIndexer()
    indexed_chats = [indexer.index_chat(c) for c in chats]

    # Build timelines
    builder = LineageBuilder()
    timelines = builder.build_all_project_timelines(indexed_chats)

    # Should have detected Aetherwright mentions
    assert "order-of-the-aetherwright" in timelines
    assert len(timelines["order-of-the-aetherwright"]) > 0
