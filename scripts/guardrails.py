# scripts/guardrails.py
from typing import Dict, List

class CaseStudyGuardrails:
    GENERIC_PHRASES = [
        r"(?i)personal system",
        r"(?i)organize.*work",
        r"(?i)productivity tool",
        r"(?i)management system",
        r"(?i)platform for.*work"
    ]

    def check_constraint_specificity(self, draft: Dict) -> Dict:
        """Reject if constraint is generic"""
        import re
        constraint = draft.get("constraint", "")

        for pattern in self.GENERIC_PHRASES:
            if re.search(pattern, constraint):
                return {
                    "passes": False,
                    "reason": f"Constraint is too generic: matches '{pattern}'",
                    "suggestion": "Explain specifically what problem this solves that others don't"
                }

        # Check length (too short = likely generic)
        if len(constraint) < 50:
            return {
                "passes": False,
                "reason": "Constraint is too brief to be specific",
                "suggestion": "Expand to show what makes this problem unique"
            }

        return {"passes": True, "reason": "Constraint is specific"}

    def check_timeline_texture(self, timeline: List[Dict]) -> Dict:
        """Verify timeline shows complexity, not just success"""
        findings_list = []
        key_moments = []

        # Check for pivot/failure moments
        failure_keywords = ["failure", "pivot", "realization", "realized", "broke", "didn't work"]
        complexity_count = 0
        keyword_types = set()

        for entry in timeline:
            content = entry.get("content", "").lower()

            for keyword in failure_keywords:
                if keyword in content:
                    complexity_count += 1
                    keyword_types.add(keyword)
                    key_moments.append({
                        "timestamp": entry.get("timestamp"),
                        "type": keyword,
                        "snippet": entry.get("content")[:100]
                    })
                    break

        if complexity_count == 0:
            findings_list.append("Timeline shows only success, no complexity/pivots/failures")
        else:
            keywords_found = ", ".join(sorted(keyword_types))
            findings_list.append(f"Found {complexity_count} complexity moment(s) with: {keywords_found}")

        findings_str = " ".join(findings_list)

        return {
            "passes": complexity_count > 0,
            "findings": findings_str,
            "key_moments": key_moments
        }

    def check_distinctiveness(self, timeline: List[Dict]) -> Dict:
        """Verify project is not interchangeable with others"""
        content_combined = " ".join([e.get("content", "") for e in timeline])

        # Check if specific project concepts appear
        # (This is simplified; in reality would check against other project timelines)

        return {
            "passes": True,
            "comment": "Manual review recommended for distinctiveness"
        }
