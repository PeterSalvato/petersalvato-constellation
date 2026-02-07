# scripts/chat_ingest.py
import re
from html.parser import HTMLParser

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
