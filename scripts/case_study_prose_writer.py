import json
import sys
from pathlib import Path

# Add scripts directory to path for imports
scripts_dir = Path(__file__).parent
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from voice_extractor import VoiceExtractor
from voice_blender import VoiceBlender
from prose_generator import ProseGenerator
from prose_guardrails import ProseGuardrails

class CaseStudyProseWriter:
    def __init__(self, skeleton_dir: str, conversation_dir: str):
        self.skeleton_dir = Path(skeleton_dir)
        self.conversation_dir = Path(conversation_dir)

        self.voice_extractor = VoiceExtractor()
        self.voice_blender = VoiceBlender()
        self.prose_generator = ProseGenerator()
        self.prose_guardrails = ProseGuardrails()

    def write_all_prose(self) -> list:
        """Write prose for all 17 projects"""

        # Step 1: Extract personal voice from conversations
        conversations = self._load_conversations()
        personal_voice = self.voice_extractor.extract_patterns(conversations)

        # Step 2: Blend with Master Builder voice
        blended_voice = self.voice_blender.blend_voices(personal_voice, {})
        voice_prompt = blended_voice.get("voice_prompt", "")

        # Step 3: Generate prose for each project
        prose_docs = []

        for skeleton_file in sorted(self.skeleton_dir.glob("*-skeleton.json")):
            with open(skeleton_file) as f:
                skeleton = json.load(f)

            project = skeleton.get("project")

            # Generate prose
            prose = self.prose_generator.generate_prose(skeleton, voice_prompt)

            # Validate quality
            validation = self.prose_guardrails.validate(prose)

            # Save prose
            prose_file = self.skeleton_dir.parent / "case-study-prose" / f"{project}-prose.md"
            prose_file.parent.mkdir(exist_ok=True)

            with open(prose_file, 'w') as f:
                f.write(prose)

            prose_docs.append({
                "project": project,
                "prose": prose,
                "validation": validation,
                "fidelity_score": self.prose_generator.validate_fidelity(prose, skeleton).get("fidelity_score", 0)
            })

        return prose_docs

    def _load_conversations(self) -> list:
        """Load all conversations for voice extraction"""
        conversations = []

        # Load from timeline JSON files (which contain the conversation content)
        for timeline_file in self.conversation_dir.glob("*-timeline.json"):
            with open(timeline_file) as f:
                timeline = json.load(f)

                # Timeline is a list of moments
                if isinstance(timeline, list):
                    for moment in timeline:
                        conversations.append({
                            "content": moment.get("content", ""),
                            "platform": moment.get("platform", "")
                        })
                else:
                    # Timeline is a dict with arc key
                    for moment in timeline.get("arc", []):
                        conversations.append({
                            "content": moment.get("content", ""),
                            "platform": moment.get("platform", "")
                        })

        return conversations
