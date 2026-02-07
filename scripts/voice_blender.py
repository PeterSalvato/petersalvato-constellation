# scripts/voice_blender.py
from typing import Dict, List

class VoiceBlender:
    MASTER_BUILDER_PRINCIPLES = {
        "directness": "Lead with what was built, not abstractions. 'I built X to solve Y.'",
        "concreteness": "Reference actual materials, constraints, structural choices. Never generalize.",
        "grounding": "Explain why through structural necessity, not aspiration.",
        "economy": "No words wasted. Every sentence earns its place.",
        "specificity": "Name the specific problem, not 'a problem'. Use actual constraints.",
        "honesty": "Show failure, pivots, dead ends. Systems survive because they handled real friction."
    }

    def blend_voices(self, personal_voice: Dict, master_builder_rules: Dict) -> Dict:
        """Blend personal voice with Master Builder principles"""

        blended = {
            "sentence_structure": personal_voice.get("sentence_structure", {}),
            "vocabulary_balance": self._blend_vocabulary(personal_voice.get("vocabulary", {})),
            "pacing": personal_voice.get("pacing", {}),
            "characteristic_phrases": personal_voice.get("characteristic_phrases", []),
            "directives": self._create_directives(personal_voice, master_builder_rules),
            "voice_prompt": self.generate_voice_prompt(personal_voice, master_builder_rules)
        }

        return blended

    def _blend_vocabulary(self, personal_vocab: Dict) -> Dict:
        """Ensure vocabulary balances technical and concrete"""
        return {
            "target_technical_ratio": max(0.10, personal_vocab.get("technical_ratio", 0.15)),
            "target_concrete_ratio": max(0.12, personal_vocab.get("concrete_ratio", 0.10)),
            "principle": "Technical enough to be precise, concrete enough to be grounded"
        }

    def _create_directives(self, personal_voice: Dict, rules: Dict) -> List[str]:
        """Create specific writing directives"""
        directives = [
            "Lead every section with what was built, not why it was needed",
            "Use actual material constraints to explain decisions",
            "Show the problem through structural gaps, not abstract statements",
            "Include moments where approach changed, prove thinking was rigorous",
            "Use your characteristic phrases where they naturally fit",
            "Match your sentence structure: " + str(personal_voice.get("sentence_structure", {}))
        ]

        return directives

    def generate_voice_prompt(self, personal_patterns: Dict, master_builder_rules: Dict) -> str:
        """Generate a prompt for prose generation"""

        phrases = personal_patterns.get("characteristic_phrases", [])
        phrases_str = ", ".join(phrases[:3]) if phrases else "insights and patterns"

        prompt = f"""Write in a voice that:

1. MASTER BUILDER PRINCIPLES (Non-negotiable):
   - Lead with what was built. Explain why through structural necessity.
   - Reference actual constraints and materials.
   - Show where approach changed. Include failures and pivots.
   - Every sentence must earn its place.
   - Grounded, concrete, honest. No marketing language.

2. YOUR VOICE (Characteristic patterns from your actual thinking):
   - Your characteristic phrases: {phrases_str}
   - Your sentence structure: {personal_patterns.get('sentence_structure', {}).get('average_sentence_length', 'moderate')} word average
   - Your pacing: {personal_patterns.get('pacing', {}).get('idea_density', 'balanced')}
   - Your style: Technical enough to be precise, concrete enough to be grounded

3. BLENDED VOICE (Master Builder + You):
   - Use your natural way of explaining, filtered through Master Builder discipline
   - Your thinking patterns become more structured and grounded
   - Concrete examples drive every explanation
   - Show the thinking process, not just the outcome
"""

        return prompt
