# scripts/chat_ingest.py
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Dict

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = []

    def handle_data(self, d):
        self.text.append(d)

    def get_data(self):
        return ''.join(self.text)

def strip_html(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_data()

class GeminiParser:
    def parse_chat(self, chat_dict):
        """Parse a single Gemini activity entry"""
        title = chat_dict.get("title", "")
        timestamp = chat_dict.get("time", "")

        # Extract HTML content
        html_content = ""
        if "safeHtmlItem" in chat_dict and chat_dict["safeHtmlItem"]:
            html_content = chat_dict["safeHtmlItem"][0].get("html", "")

        # Strip HTML tags
        content = strip_html(html_content) if html_content else ""

        return {
            "title": title,
            "timestamp": timestamp,
            "content": content,
            "platform": "gemini"
        }

class ChatGPTParser:
    def parse_conversation(self, conversation_dict):
        """Parse a single ChatGPT conversation export"""
        # Extract conversation title
        title = conversation_dict.get("name", "")

        # Extract timestamp from first message or created_at
        timestamp = self._extract_timestamp(conversation_dict)

        # Extract and concatenate all message content
        content = self._extract_content(conversation_dict)

        return {
            "title": title,
            "timestamp": timestamp,
            "content": content,
            "platform": "chatgpt"
        }

    def _extract_timestamp(self, conversation_dict):
        """Extract timestamp from conversation"""
        # ChatGPT stores created_at at conversation level
        created_at = conversation_dict.get("created_at", "")
        if created_at:
            return created_at

        # Fallback: try to get timestamp from first message
        messages = conversation_dict.get("chat_messages", [])
        if messages and messages[0].get("created_at"):
            return messages[0]["created_at"]

        return ""

    def _extract_content(self, conversation_dict):
        """Extract and concatenate all conversation messages"""
        messages = conversation_dict.get("chat_messages", [])
        content_parts = []

        for message in messages:
            sender = message.get("sender", "unknown")

            # Extract text content from the message
            text = ""
            if message.get("text"):
                text = message.get("text")
            elif message.get("content"):
                # content is an array of content blocks
                content_blocks = message.get("content", [])
                text_parts = []
                for block in content_blocks:
                    if block.get("type") == "text" and block.get("text"):
                        text_parts.append(block.get("text"))
                text = "".join(text_parts)

            if text.strip():  # Only include non-empty messages
                content_parts.append(f"{sender}: {text}")

        return "\n\n".join(content_parts)

class ClaudeParser:
    def parse_conversation(self, conversation_dict):
        """Parse a single Claude conversation export"""
        # Extract conversation title
        title = conversation_dict.get("title", "")

        # Extract timestamp from create_time
        timestamp = self._extract_timestamp(conversation_dict)

        # Extract and concatenate all message content
        content = self._extract_content(conversation_dict)

        return {
            "title": title,
            "timestamp": timestamp,
            "content": content,
            "platform": "claude"
        }

    def _extract_timestamp(self, conversation_dict):
        """Extract timestamp from conversation"""
        # Claude stores create_time as Unix timestamp (float)
        create_time = conversation_dict.get("create_time")
        if create_time is None:
            return ""

        # Convert Unix timestamp to ISO 8601 format
        try:
            from datetime import datetime
            dt = datetime.fromtimestamp(float(create_time))
            return dt.isoformat()
        except (ValueError, TypeError):
            return ""

    def _extract_content(self, conversation_dict):
        """Extract and concatenate all conversation messages"""
        mapping = conversation_dict.get("mapping", {})
        content_parts = []

        # Claude stores messages in a tree structure via mapping
        # Each node has a message field and parent/children pointers
        for node_id, node in mapping.items():
            if not node.get("message"):
                continue

            message = node["message"]
            role = message.get("author", {}).get("role")

            # Only include user and assistant messages (skip system messages)
            if role not in ["user", "assistant"]:
                continue

            # Extract content from parts array
            content_obj = message.get("content", {})
            parts = content_obj.get("parts", [])

            # Join all parts (usually just one, but handle multiple)
            text = ""
            if parts:
                text_parts = [p for p in parts if isinstance(p, str)]
                text = "".join(text_parts)

            # Only include non-empty messages
            if text.strip():
                content_parts.append(f"{role}: {text}")

        return "\n\n".join(content_parts)

class ChatExportLoader:
    def __init__(self):
        self.gemini_parser = GeminiParser()
        self.chatgpt_parser = ChatGPTParser()
        self.claude_parser = ClaudeParser()

    def load_gemini(self, filepath: str) -> List[Dict]:
        """Load and parse Gemini activity export"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Gemini exports as array of activity items
        chats = []
        for item in data:
            parsed = self.gemini_parser.parse_chat(item)
            chats.append(parsed)

        return chats

    def load_chatgpt(self, filepath: str) -> List[Dict]:
        """Load and parse ChatGPT conversation export"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # ChatGPT exports as array of conversations
        chats = []
        for conversation in data:
            parsed = self.chatgpt_parser.parse_conversation(conversation)
            chats.append(parsed)

        return chats

    def load_claude(self, filepath: str) -> List[Dict]:
        """Load and parse Claude conversation export"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Claude exports as array of conversations
        chats = []
        for conversation in data:
            parsed = self.claude_parser.parse_conversation(conversation)
            chats.append(parsed)

        return chats

    def load_all_exports(self, gemini_path: str, chatgpt_path: str, claude_path: str):
        """Load all three exports and combine"""
        all_chats = []

        # Load Gemini
        gemini_chats = self.load_gemini(gemini_path)
        all_chats.extend(gemini_chats)

        # Load ChatGPT
        chatgpt_chats = self.load_chatgpt(chatgpt_path)
        all_chats.extend(chatgpt_chats)

        # Load Claude
        claude_chats = self.load_claude(claude_path)
        all_chats.extend(claude_chats)

        return all_chats
