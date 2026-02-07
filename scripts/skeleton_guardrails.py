import re
from typing import Dict, List, Any


class SkeletonGuardrails:
    """Validation class to prevent skeleton flattening and ensure depth."""

    # Generic phrases that indicate lack of specificity
    GENERIC_PATTERNS = [
        r"personal\s+system",
        r"organize.*work",
        r"productivity\s+tool",
        r"management\s+system",
    ]

    # Minimum texture score required for complexity
    MIN_TEXTURE_SCORE = 0.3

    # Minimum unique arc moment types required
    MIN_ARC_DIVERSITY = 3

    # Minimum constraint length (characters)
    MIN_CONSTRAINT_LENGTH = 50

    def __init__(self):
        """Initialize the guardrails validator."""
        self.compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.GENERIC_PATTERNS]

    def validate(self, skeleton: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate a skeleton against guardrails.

        Args:
            skeleton: Dictionary with keys: project, constraint, arc, texture_score

        Returns:
            Dictionary with:
                - passes: bool indicating if skeleton passes all checks
                - issues: list of validation issue strings
                - texture_score: float
                - constraint_length: int
                - arc_diversity: int (count of unique arc types)
        """
        issues = []

        # Extract skeleton components
        constraint = skeleton.get("constraint", "")
        arc = skeleton.get("arc", [])
        texture_score = skeleton.get("texture_score", 0.0)

        # Check 1: Constraint specificity (reject if generic OR too short)
        if self._is_generic_constraint(constraint) or len(constraint) < self.MIN_CONSTRAINT_LENGTH:
            issues.append(
                f"Generic or too-short constraint: '{constraint[:50]}...' "
                f"(length: {len(constraint)}, min: {self.MIN_CONSTRAINT_LENGTH})"
            )

        # Check 2: Texture score (reject if below minimum)
        if texture_score < self.MIN_TEXTURE_SCORE:
            issues.append(
                f"Texture score too low: {texture_score:.2f} (min: {self.MIN_TEXTURE_SCORE})"
            )

        # Check 3: Arc diversity (reject if insufficient unique types)
        arc_diversity = self._count_unique_arc_types(arc)
        if arc_diversity < self.MIN_ARC_DIVERSITY:
            issues.append(
                f"Insufficient arc diversity: {arc_diversity} unique types "
                f"(min: {self.MIN_ARC_DIVERSITY}, need at least: genesis → problem → solution)"
            )

        return {
            "passes": len(issues) == 0,
            "issues": issues,
            "texture_score": texture_score,
            "constraint_length": len(constraint),
            "arc_diversity": arc_diversity
        }

    def _is_generic_constraint(self, constraint: str) -> bool:
        """Check if constraint matches generic patterns."""
        for pattern in self.compiled_patterns:
            if pattern.search(constraint):
                return True
        return False

    def _count_unique_arc_types(self, arc: List[Dict[str, Any]]) -> int:
        """Count unique moment types in the arc."""
        unique_types = set()
        for moment in arc:
            moment_type = moment.get("type")
            if moment_type:
                unique_types.add(moment_type)
        return len(unique_types)
