import re
from typing import Dict, List


class SemanticIndexer:
    # Project patterns with confidence levels
    PROJECT_PATTERNS = {
        # Tier 1: Protocols
        "order-of-the-aetherwright": {
            "high": [
                r"(?i)aetherwright",
                r"(?i)order of the æ",
                r"(?i)sovereign cognition",
                r"(?i)ritual framework"
            ],
            "medium": [
                r"(?i)symbolic operating system",
                r"(?i)intentional work"
            ]
        },
        "savepoint-protocol": {
            "high": [
                r"(?i)semantic turning point",
                r"(?i)realization clicked"
            ],
            "medium": [
                r"(?i)savepoint",
                r"(?i)mark where.*changed",
                r"(?i)cognitive inflection"
            ]
        },
        "ai-devops-workbench": {
            "high": [
                r"(?i)ai devops",
                r"(?i)vibecoding",
                r"(?i)architectural decisions"
            ],
            "medium": [
                r"(?i)institutional memory",
                r"(?i)context loss.*agent"
            ]
        },
        "portable-agency": {
            "high": [
                r"(?i)portable agency",
                r"(?i)self-discovering.*specialist",
                r"(?i)tech stack.*detection",
                r"(?i)project manager.*tech lead.*frontend.*backend"
            ],
            "medium": [
                r"(?i)agent.*verif",
                r"(?i)zero configuration.*detection",
                r"(?i)built-in verification"
            ]
        },
        # Tier 2: Applied Systems
        "aiden-jae": {
            "high": [
                r"(?i)aiden.?jae",
                r"(?i)luxury.*jewelry",
                r"(?i)tropical.*organic"
            ],
            "medium": [
                r"(?i)south florida.*texture",
                r"(?i)organic.*luxury"
            ]
        },
        "altrueism": {
            "high": [
                r"(?i)altrueism",
                r"(?i)brand remediation",
                r"(?i)handcrafted.*artisanal",
                r"(?i)gaudy.*apparel"
            ],
            "medium": [
                r"(?i)aesthetic remediation",
                r"(?i)artisanal.*positioning"
            ]
        },
        "everyday-gold": {
            "high": [
                r"(?i)everyday gold",
                r"(?i)natural deodorant",
                r"(?i)aiden jae.*umbrella"
            ],
            "medium": [
                r"(?i)deodorant.*branding",
                r"(?i)sister.*company"
            ]
        },
        "encore": {
            "high": [
                r"(?i)enterprise platform",
                r"(?i)windows forms.*web",
                r"(?i)40,000.*users"
            ],
            "medium": [
                r"(?i)stewardship.*scale",
                r"(?i)99\.9%.*uptime"
            ]
        },
        "modernist-homestead": {
            "high": [
                r"(?i)modernist homestead",
                r"(?i)neurodivergent.*scaffolding",
                r"(?i)home system"
            ],
            "medium": [
                r"(?i)hydroponics.*mycology",
                r"(?i)modernist cooking"
            ]
        },
        # Tier 3: Practice
        "echo-and-bone": {
            "high": [
                r"(?i)echo.?and.?bone",
                r"(?i)stoic.*philosophy",
                r"(?i)poster series.*stoic"
            ],
            "medium": [
                r"(?i)engraving.*black letter",
                r"(?i)three.?part.*poster",
                r"(?i)grid.*philosophy"
            ]
        },
        "mathontape": {
            "high": [
                r"(?i)mathontape",
                r"(?i)electronic music.*branding",
                r"(?i)cassette.*futurism",
                r"(?i)dot matrix"
            ],
            "medium": [
                r"(?i)retro.?futuristic",
                r"(?i)music production.*branding"
            ]
        },
        "photogeography": {
            "high": [
                r"(?i)photogeography",
                r"(?i)grid system.*information",
                r"(?i)qr code.*location",
                r"(?i)latitude.*longitude"
            ],
            "medium": [
                r"(?i)photograph.*metadata",
                r"(?i)poster.*grid.*data"
            ]
        },
        "versagrams": {
            "high": [
                r"(?i)versagrams",
                r"(?i)song lyrics.*generative",
                r"(?i)grid.*lyrics.*ai"
            ],
            "medium": [
                r"(?i)lyrics.*artwork.*grid",
                r"(?i)poetic.*constraint"
            ]
        },
        "the-deep-cuts": {
            "high": [
                r"(?i)the.?deep.?cuts",
                r"(?i)dj.*methodology",
                r"(?i)music appreciation.*book"
            ],
            "medium": [
                r"(?i)dj.*curation",
                r"(?i)music.*methodology"
            ]
        },
        "cryptozoology": {
            "high": [
                r"(?i)cryptozoology"
            ],
            "medium": [
                r"(?i)mythology.*research",
                r"(?i)research methodology"
            ]
        },
        "monstrum": {
            "high": [
                r"(?i)monstrum"
            ],
            "medium": [
                r"(?i)design.*visual"
            ]
        },
        "motorology": {
            "high": [
                r"(?i)motorology"
            ],
            "medium": [
                r"(?i)automotive.*system",
                r"(?i)motor.*design"
            ]
        },
        "everyday-gold-practice": {
            "high": [
                r"(?i)everyday gold.*practice",
                r"(?i)deodorant.*product.*research"
            ],
            "medium": [
                r"(?i)product research.*deodorant",
                r"(?i)everyday gold.*experiment"
            ]
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
