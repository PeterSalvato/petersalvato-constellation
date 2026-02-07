from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class NarrativeSkeleton:
    """Represents the skeletal structure of a narrative built from moments."""
    project: str
    constraint: str
    arc: List[Dict]
    platforms: Dict[str, int] = field(default_factory=dict)
    timeline_span: str = ""
    texture_score: float = 0.0
    source_snippets: List[str] = field(default_factory=list)


class NarrativeBuilder:
    """Builds narrative skeletons from extracted moments."""

    def __init__(self):
        """Initialize the narrative builder."""
        pass

    def build_skeleton(self, project_id: str, moments: List[Dict]) -> NarrativeSkeleton:
        """
        Build a narrative skeleton from a list of moments.

        Args:
            project_id: Identifier for the project
            moments: List of moment dictionaries with type, timestamp, snippet

        Returns:
            NarrativeSkeleton object with complete narrative structure
        """
        # Build the chronological arc
        arc = self._build_arc(moments)

        # Extract the constraint from genesis + problem moments
        constraint = self._identify_constraint(moments)

        # Count platforms in moments
        platforms = self._count_platforms(moments)

        # Calculate texture score based on diversity and types
        texture_score = self._calculate_texture(moments)

        # Extract timeline span
        timeline_span = self._extract_timeline_span(arc)

        # Extract source snippets
        source_snippets = [m.get("snippet", "") for m in arc if m.get("snippet")]

        return NarrativeSkeleton(
            project=project_id,
            constraint=constraint,
            arc=arc,
            platforms=platforms,
            timeline_span=timeline_span,
            texture_score=texture_score,
            source_snippets=source_snippets
        )

    def _identify_constraint(self, moments: List[Dict]) -> str:
        """
        Extract the constraint (problem) from genesis and problem moments.

        Args:
            moments: List of moment dictionaries

        Returns:
            String describing the constraint/problem the system solves
        """
        # Look for genesis and problem moments
        genesis_snippets = []
        problem_snippets = []

        for moment in moments:
            moment_type = moment.get("type", "").lower()
            snippet = moment.get("snippet", "")

            if moment_type == "genesis" and snippet:
                genesis_snippets.append(snippet)
            elif moment_type == "problem" and snippet:
                problem_snippets.append(snippet)

        # Combine to form constraint
        if genesis_snippets and problem_snippets:
            return f"{genesis_snippets[0]} — {problem_snippets[0]}"
        elif genesis_snippets:
            return genesis_snippets[0]
        elif problem_snippets:
            return problem_snippets[0]
        else:
            return "Project evolving through moments"

    def _build_arc(self, moments: List[Dict]) -> List[Dict]:
        """
        Build chronological arc of moments, preserving all fields.

        Args:
            moments: List of moment dictionaries with timestamp field

        Returns:
            Chronologically sorted list of moments with all original fields preserved
        """
        # Sort by timestamp
        def parse_timestamp(moment):
            timestamp_str = moment.get("timestamp", "")
            try:
                return datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                return datetime.min

        sorted_moments = sorted(moments, key=parse_timestamp)
        return sorted_moments

    def _count_platforms(self, moments: List[Dict]) -> Dict[str, int]:
        """
        Count moments by platform.

        Args:
            moments: List of moment dictionaries with platform field

        Returns:
            Dictionary mapping platform names to counts
        """
        platforms = {}
        for moment in moments:
            platform = moment.get("platform", "unknown")
            platforms[platform] = platforms.get(platform, 0) + 1
        return platforms

    def _calculate_texture(self, moments: List[Dict]) -> float:
        """
        Calculate texture score based on moment type diversity.

        Scoring:
        - +0.3 if has PIVOT
        - +0.2 if has PROBLEM
        - +0.2 if has REFINEMENT
        - +0.3 * (unique_types / 8) for diversity bonus
        - Cap at 1.0

        Args:
            moments: List of moment dictionaries with type field

        Returns:
            Texture score between 0.0 and 1.0
        """
        texture = 0.0
        moment_types = set()

        # Count moment types
        for moment in moments:
            moment_type = moment.get("type", "").lower()
            moment_types.add(moment_type)

            if moment_type == "pivot":
                texture += 0.3
            elif moment_type == "problem":
                texture += 0.2
            elif moment_type == "refinement":
                texture += 0.2

        # Diversity bonus: up to 0.3 points for unique types
        unique_types = len(moment_types)
        max_types = 8  # Number of moment types in MomentType enum
        diversity_bonus = 0.3 * (unique_types / max_types)
        texture += diversity_bonus

        # Cap at 1.0
        return min(texture, 1.0)

    def _extract_timeline_span(self, arc: List[Dict]) -> str:
        """
        Extract timeline span from first to last moment.

        Args:
            arc: Chronologically sorted list of moments

        Returns:
            String describing timeline span (e.g., "2024-09-30 to 2024-11-01")
        """
        if not arc:
            return ""

        first_timestamp = arc[0].get("timestamp", "")
        last_timestamp = arc[-1].get("timestamp", "")

        # Format timestamps for display (extract just the date part)
        def format_timestamp(ts):
            if "T" in ts:
                return ts.split("T")[0]
            return ts

        if first_timestamp and last_timestamp:
            return f"{format_timestamp(first_timestamp)} to {format_timestamp(last_timestamp)}"
        return ""
