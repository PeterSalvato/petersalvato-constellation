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

class ChatExportLoader:
    def __init__(self):
        self.gemini_parser = GeminiParser()

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

    def load_all_exports(self, gemini_path: str, chatgpt_path: str, claude_path: str):
        """Load all three exports and combine"""
        all_chats = []

        # Load Gemini
        gemini_chats = self.load_gemini(gemini_path)
        all_chats.extend(gemini_chats)

        # TODO: Add ChatGPT loader
        # TODO: Add Claude loader

        return all_chats
