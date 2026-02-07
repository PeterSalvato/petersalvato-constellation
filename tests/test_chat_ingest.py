# tests/test_chat_ingest.py
import json
from scripts.chat_ingest import GeminiParser, ChatExportLoader

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
