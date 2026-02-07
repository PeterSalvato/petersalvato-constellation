# scripts/prose_guardrails.py
import re
from typing import Dict, List

class ProseGuardrails:
    GENERIC_PHRASES = [
        r"(?i)system for.*work|system to.*work",
        r"(?i)help.*organize|help.*manage",
        r"(?i)productivity tool|management system",
        r"(?i)to.*better|to.*improve",
        r"(?i)streamline|optimize|enhance",
        r"(?i)for.*teams|for.*collaboration"
    ]

    MARKETING_LANGUAGE = [
        r"(?i)innovative|revolutionary|groundbreaking",
        r"(?i)empower|synergize|leverage",
        r"(?i)next-generation|cutting-edge|paradigm",
        r"(?i)seamless|effortless|magical"
    ]

    REQUIRED_ELEMENTS = {
        "specific_problem": [
            r"(?i)problem\s*:|the.*gap|didn't.*work",
            r"(?i)missing|broken|constraint"
        ],
        "concrete_solution": [
            r"(?i)built|created|designed|implemented",
            r"(?i)uses.*\(|structure|format"
        ],
        "thinking_evolution": [
            r"(?i)pivot|realized|tried.*instead",
            r"(?i)failed|changed.*approach"
        ]
    }

    def validate(self, prose: str) -> Dict:
        """Validate prose quality"""

        issues = []
        has_elements = {}

        # Check for generic phrases
        for pattern in self.GENERIC_PHRASES:
            if re.search(pattern, prose):
                issues.append(f"Generic phrase detected: {pattern}")
                break

        # Check for marketing language
        for pattern in self.MARKETING_LANGUAGE:
            if re.search(pattern, prose):
                issues.append(f"Marketing language detected: {pattern}")
                break

        # Check for required elements
        for element, patterns in self.REQUIRED_ELEMENTS.items():
            found = any(re.search(p, prose) for p in patterns)
            has_elements[element] = found
            if not found:
                issues.append(f"Missing: {element}")

        # Check for Master Builder voice indicators
        master_builder_indicators = [
            r"(?i)built|created|designed",
            r"(?i)problem|constraint|gap",
            r"(?i)structure|material|concrete"
        ]

        indicators_found = sum(1 for p in master_builder_indicators if re.search(p, prose))

        if indicators_found < 2:
            issues.append("Lacks Master Builder voice (missing concrete/structural language)")

        return {
            "passes": len(issues) == 0,
            "issues": issues,
            "has_elements": has_elements,
            "voice_strength": indicators_found / len(master_builder_indicators)
        }
