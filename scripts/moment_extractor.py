from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import re
from typing import List, Optional


class MomentType(Enum):
    """Types of moments representing inflection points in thinking."""
    GENESIS = "genesis"  # Initial ideas, starting points
    REALIZATION = "realization"  # New insights or understanding
    PROBLEM = "problem"  # Issues, blockers, gaps discovered
    PIVOT = "pivot"  # Changes in approach or direction
    REFINEMENT = "refinement"  # Improvements and iterations
    INTEGRATION = "integration"  # Combining ideas or components
    VALIDATION = "validation"  # Verification, testing, confirmation
    ARTIFACT = "artifact"  # Creation of outputs or deliverables


@dataclass
class Moment:
    """Represents a moment - an inflection point in thinking."""
    type: MomentType
    timestamp: str
    content: str
    platform: str
    snippet: str
    title: Optional[str] = None


class MomentExtractor:
    """Extracts moments from timeline entries to identify narrative inflection points."""

    # Patterns for detecting moment types in content
    PROJECT_PATTERNS = {
        MomentType.GENESIS: [
            r"first\s+(?:thought|idea|concept|approach)",
            r"initial\s+(?:thought|idea|concept|approach)",
            r"started\s+with",
            r"began\s+with",
            r"origin(?:al)?.*idea",
            r"need(?:ed)?.*way",
            r"want(?:ed)?.*way",
            r"i\s+need",
            r"marking.*(?:where|place|point)",
        ],
        MomentType.REALIZATION: [
            r"realized",
            r"understood",
            r"figured\s+out",
            r"discovered",
            r"insight",
            r"suddenly",
            r"it\s+clicked",
            r"became\s+clear",
            r"see.*pattern",
            r"see.*connection",
        ],
        MomentType.PROBLEM: [
            r"didn't\s+work",
            r"broke",
            r"broken",
            r"missing",
            r"gap",
            r"problem",
            r"issue",
            r"error",
            r"failed",
            r"doesn't\s+work",
            r"wasn't\s+working",
            r"didn't\s+match",
            r"too\s+(?:slow|complex|simple)",
        ],
        MomentType.PIVOT: [
            r"pivot",
            r"changed.*approach",
            r"different.*approach",
            r"tried.*instead",
            r"switched\s+to",
            r"instead\s+of",
            r"rather\s+than",
            r"but\s+that\s+didn't\s+work",
            r"then\s+(?:i|we)\s+realized",
        ],
        MomentType.REFINEMENT: [
            r"improved",
            r"refined",
            r"optimized",
            r"simplified",
            r"streamlined",
            r"reduced",
            r"enhanced",
            r"better\s+(?:way|approach)",
            r"made.*more",
            r"adjusted",
            r"tuned",
        ],
        MomentType.INTEGRATION: [
            r"integrated",
            r"combined",
            r"merged",
            r"connected",
            r"linked",
            r"brought\s+together",
            r"unified",
            r"assembled",
            r"put.*together",
        ],
        MomentType.VALIDATION: [
            r"tested",
            r"validated",
            r"verified",
            r"confirmed",
            r"works",
            r"it\s+works",
            r"proved",
            r"evidence",
            r"checked",
            r"works\s+(?:great|well)",
        ],
        MomentType.ARTIFACT: [
            r"created",
            r"built",
            r"wrote",
            r"designed",
            r"developed",
            r"implemented",
            r"launched",
            r"released",
            r"published",
            r"made.*tool",
            r"wrote.*(?:script|function|class)",
        ],
    }

    def __init__(self):
        """Initialize the moment extractor with compiled regex patterns."""
        self.compiled_patterns = {}
        for moment_type, patterns in self.PROJECT_PATTERNS.items():
            self.compiled_patterns[moment_type] = [
                re.compile(pattern, re.IGNORECASE) for pattern in patterns
            ]

    def extract_moments(self, timeline: List[dict]) -> List[Moment]:
        """
        Extract moments from a list of timeline entries.

        Args:
            timeline: List of timeline entry dictionaries with keys:
                     title, timestamp, content, platform

        Returns:
            List of Moment objects representing inflection points
        """
        moments = []

        for entry in timeline:
            content = entry.get("content", "")
            if not content:
                continue

            moment_type = self.detect_moment_type(content)

            # Only extract if a moment type was detected
            if moment_type:
                snippet = self._extract_snippet(content)
                moment = Moment(
                    type=moment_type,
                    timestamp=entry.get("timestamp", ""),
                    content=content,
                    platform=entry.get("platform", ""),
                    snippet=snippet,
                    title=entry.get("title")
                )
                moments.append(moment)

        return moments

    def detect_moment_type(self, content: str) -> Optional[MomentType]:
        """
        Detect the type of moment from content text.

        Args:
            content: Text content to analyze

        Returns:
            MomentType if detected, None otherwise
        """
        if not content:
            return None

        # Try to match patterns in order of specificity
        # PIVOT is more specific than PROBLEM, so check it first
        for moment_type in [
            MomentType.PIVOT,
            MomentType.PROBLEM,
            MomentType.GENESIS,
            MomentType.REALIZATION,
            MomentType.VALIDATION,
            MomentType.ARTIFACT,
            MomentType.INTEGRATION,
            MomentType.REFINEMENT,
        ]:
            patterns = self.compiled_patterns[moment_type]
            for pattern in patterns:
                if pattern.search(content):
                    return moment_type

        return None

    def _extract_snippet(self, content: str, max_length: int = 150) -> str:
        """
        Extract a meaningful snippet from content.

        Args:
            content: Full text content
            max_length: Maximum snippet length (default 150 chars)

        Returns:
            Snippet of 50-150 characters, preferring sentence boundaries
        """
        if len(content) <= max_length:
            return content.strip()

        # Try to find a good breaking point (period, comma, or space)
        min_length = 50
        snippet = content[:max_length]

        # Look for a sentence break (period + space)
        period_idx = snippet.rfind(". ")
        if period_idx > min_length:
            return content[:period_idx + 1].strip()

        # Look for a comma
        comma_idx = snippet.rfind(", ")
        if comma_idx > min_length:
            return content[:comma_idx + 1].strip()

        # Fall back to space
        space_idx = snippet.rfind(" ")
        if space_idx > min_length:
            return content[:space_idx].strip() + "..."

        return snippet.strip() + "..."
