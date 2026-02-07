import re
from typing import Dict, List


class SemanticIndexer:
    # Project patterns with confidence levels
    PROJECT_PATTERNS = {
        "order-of-the-aetherwright": {
            "high": [
                r"(?i)aetherwright",
                r"(?i)order of the æ",
                r"(?i)sovereign cognition",
                r"(?i)ritual framework"
            ],
            "medium": []
        },
        "savepoint-protocol": {
            "high": [
                r"(?i)semantic turning point",
                r"(?i)realization clicked"
            ],
            "medium": [
                r"(?i)savepoint",
                r"(?i)mark where.*changed"
            ]
        },
        "ai-devops-workbench": {
            "high": [
                r"(?i)ai devops",
                r"(?i)vibecoding",
                r"(?i)architectural decisions"
            ],
            "medium": []
        },
        "encore": {
            "high": [
                r"(?i)enterprise platform",
                r"(?i)windows forms.*web",
                r"(?i)40,000.*users"
            ],
            "medium": []
        },
        "aiden-jae": {
            "high": [
                r"(?i)aiden.?jae",
                r"(?i)luxury.*jewelry",
                r"(?i)tropical.*organic"
            ],
            "medium": []
        },
        "modernist-homestead": {
            "high": [
                r"(?i)modernist homestead",
                r"(?i)neurodivergent.*scaffolding",
                r"(?i)home system"
            ],
            "medium": []
        }
    }

    def detect_projects(self, chat: Dict) -> Dict:
        """Detect which projects are mentioned in a chat"""
        title = chat.get("title", "")
        content = chat.get("content", "")
        full_text = f"{title} {content}"

        detected = {}

        for project_id, confidence_levels in self.PROJECT_PATTERNS.items():
            # Check high confidence patterns first
            for pattern in confidence_levels["high"]:
                if re.search(pattern, full_text):
                    if project_id not in detected:
                        detected[project_id] = {
                            "confidence": "high",
                            "matched_pattern": pattern
                        }
                    break

            # If not detected with high confidence, check medium confidence
            if project_id not in detected:
                for pattern in confidence_levels["medium"]:
                    if re.search(pattern, full_text):
                        detected[project_id] = {
                            "confidence": "medium",
                            "matched_pattern": pattern
                        }
                        break

        return detected

    def index_chat(self, chat: Dict) -> Dict:
        """Add project detection to a chat"""
        chat["detected_projects"] = self.detect_projects(chat)
        return chat
