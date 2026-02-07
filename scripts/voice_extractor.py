# scripts/voice_extractor.py
from typing import Dict, List
import re
from collections import Counter

class VoiceExtractor:
    def __init__(self):
        # Patterns for identifying voice characteristics
        self.STRUCTURAL_PATTERNS = {
            "short_declarative": r"^[A-Z][^.!?]{10,30}\.$",
            "setup_then_detail": r"[^.!?]+\.\s+[A-Z][^.!?]*\.",
            "parallel_structure": r"(\w+\s+[\w\s]+),\s+(\w+\s+[\w\s]+),\s+(\w+\s+[\w\s]+)"
        }

        self.CHARACTERISTIC_PHRASES = [
            "the real (insight|problem|tension)",
            "what (actually|really) (matters|happens)",
            "the (gap|difference|tension) (between|is)",
            "if you (own|control|understand)",
            "this (survives|fails|breaks) because",
            "the (pattern|lesson|insight) (is|shows)",
            "you need (to|a way to)",
            "the key (insight|difference|tension)"
        ]

        self.METAPHOR_CATEGORIES = {
            "structural": r"(scaffold|foundation|pillar|frame|architecture|system)",
            "material": r"(material|concrete|surface|texture|solid|durable)",
            "flow": r"(flow|current|stream|movement|drift|shift)",
            "visibility": r"(see|visible|clear|transparent|obscured|hidden)"
        }

    def extract_patterns(self, conversations: List[Dict]) -> Dict:
        """Extract voice patterns from conversations"""

        all_content = " ".join([c.get("content", "") for c in conversations])

        patterns = {
            "sentence_structure": self._analyze_sentence_structure(all_content),
            "vocabulary": self._analyze_vocabulary(all_content),
            "metaphors": self._identify_metaphor_preferences(all_content),
            "pacing": self._analyze_pacing(all_content),
            "characteristic_phrases": self.identify_characteristic_phrases(conversations)
        }

        return patterns

    def _analyze_sentence_structure(self, content: str) -> Dict:
        """Identify sentence structure patterns"""
        sentences = re.split(r'[.!?]+', content)

        avg_length = sum(len(s.split()) for s in sentences) / len(sentences)

        return {
            "average_sentence_length": avg_length,
            "uses_short_declaratives": any(re.match(self.STRUCTURAL_PATTERNS["short_declarative"], s) for s in sentences),
            "uses_parallel_structure": any(re.search(self.STRUCTURAL_PATTERNS["parallel_structure"], s) for s in sentences)
        }

    def _analyze_vocabulary(self, content: str) -> Dict:
        """Identify vocabulary preferences"""
        words = content.lower().split()

        # Technical vs. accessible vocabulary balance
        technical_words = [w for w in words if re.match(r'(architecture|system|pattern|constraint|framework|protocol)', w)]
        concrete_words = [w for w in words if re.match(r'(material|physical|surface|touch|see|build|make)', w)]

        return {
            "technical_ratio": len(technical_words) / len(words) if words else 0,
            "concrete_ratio": len(concrete_words) / len(words) if words else 0,
            "vocabulary_diversity": len(set(words)) / len(words) if words else 0
        }

    def _identify_metaphor_preferences(self, content: str) -> Dict:
        """Identify metaphor and analogy patterns"""
        metaphors = {}

        for category, pattern in self.METAPHOR_CATEGORIES.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            metaphors[category] = len(matches)

        return metaphors

    def _analyze_pacing(self, content: str) -> Dict:
        """Analyze pace of idea development"""
        paragraphs = content.split('\n\n')

        return {
            "average_paragraph_length": sum(len(p.split()) for p in paragraphs) / len(paragraphs) if paragraphs else 0,
            "idea_density": "high" if sum(len(p.split()) for p in paragraphs) / len(paragraphs) > 100 else "moderate"
        }

    def identify_characteristic_phrases(self, conversations: List[Dict]) -> List[str]:
        """Find phrases characteristic of your voice"""
        all_content = " ".join([c.get("content", "") for c in conversations])

        found_phrases = []
        for phrase_pattern in self.CHARACTERISTIC_PHRASES:
            if re.search(phrase_pattern, all_content, re.IGNORECASE):
                found_phrases.append(phrase_pattern)

        return found_phrases
