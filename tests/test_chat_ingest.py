# tests/test_chat_ingest.py
import json
from scripts.chat_ingest import GeminiParser, ChatGPTParser, ClaudeParser, ChatExportLoader

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

def test_claude_parser_extracts_title():
    """Test basic title and timestamp extraction from Claude conversation"""
    sample_claude = {
        "title": "STEM Challenge Idea Vetting",
        "create_time": 1768601279.523608,
        "update_time": 1768612641.677551,
        "mapping": {
            "node1": {
                "message": {
                    "id": "msg1",
                    "author": {"role": "user"},
                    "content": {
                        "content_type": "text",
                        "parts": ["Hello Claude"]
                    }
                }
            },
            "node2": {
                "message": {
                    "id": "msg2",
                    "author": {"role": "assistant"},
                    "content": {
                        "content_type": "text",
                        "parts": ["Hello! How can I help?"]
                    }
                }
            }
        }
    }

    parser = ClaudeParser()
    result = parser.parse_conversation(sample_claude)

    assert result["title"] == "STEM Challenge Idea Vetting"
    assert result["platform"] == "claude"
    assert result["timestamp"]  # Should have ISO format timestamp
    assert "2026-01-16" in result["timestamp"]  # Date portion
    assert "user: Hello Claude" in result["content"]
    assert "assistant: Hello! How can I help?" in result["content"]

def test_claude_parser_filters_system_messages():
    """Test that system messages are filtered out"""
    sample_claude = {
        "title": "Test",
        "create_time": 1768601279.523608,
        "mapping": {
            "system_node": {
                "message": {
                    "author": {"role": "system"},
                    "content": {"content_type": "text", "parts": ["System message"]}
                }
            },
            "user_node": {
                "message": {
                    "author": {"role": "user"},
                    "content": {"content_type": "text", "parts": ["User message"]}
                }
            }
        }
    }

    parser = ClaudeParser()
    result = parser.parse_conversation(sample_claude)

    assert "system:" not in result["content"]
    assert "user: User message" in result["content"]

def test_claude_parser_handles_empty_conversations():
    """Test handling of conversations with no user/assistant messages"""
    sample_claude = {
        "title": "Empty conversation",
        "create_time": 1768601279.523608,
        "mapping": {
            "root": {
                "message": None
            }
        }
    }

    parser = ClaudeParser()
    result = parser.parse_conversation(sample_claude)

    assert result["title"] == "Empty conversation"
    assert result["content"] == ""

def test_claude_parser_handles_multipart_messages():
    """Test handling of messages with multiple parts"""
    sample_claude = {
        "title": "Multipart test",
        "create_time": 1768601279.523608,
        "mapping": {
            "multipart_node": {
                "message": {
                    "author": {"role": "user"},
                    "content": {
                        "content_type": "text",
                        "parts": ["Part 1", " Part 2", " Part 3"]
                    }
                }
            }
        }
    }

    parser = ClaudeParser()
    result = parser.parse_conversation(sample_claude)

    assert "user: Part 1 Part 2 Part 3" in result["content"]

def test_load_claude_export():
    """Test loading actual Claude conversation export"""
    loader = ChatExportLoader()
    chats = loader.load_claude(
        "/home/peter/homelab/knowledge/exports/7bb7d7448a4fe8b37c10d84958a3011b01d3dc5d3b4a88cb8a89ceea3ebda027-2026-01-22-18-47-51-f068f48a77d44e359188dc77169ae29d/conversations.json"
    )

    assert isinstance(chats, list)
    assert len(chats) > 0
    assert all("timestamp" in c for c in chats)
    assert all("content" in c for c in chats)
    assert all("title" in c for c in chats)
    assert all(c["platform"] == "claude" for c in chats)

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
