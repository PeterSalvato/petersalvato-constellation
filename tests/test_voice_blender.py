# tests/test_voice_blender.py
from scripts.voice_blender import VoiceBlender

def test_blend_voices():
    blender = VoiceBlender()

    personal_voice = {
        "sentence_structure": {"average_sentence_length": 18},
        "vocabulary": {"technical_ratio": 0.15, "concrete_ratio": 0.12},
        "pacing": {"idea_density": "high"},
        "characteristic_phrases": ["the real insight", "what actually matters"]
    }

    master_builder_rules = {
        "directness": "lead with what was built",
        "concreteness": "reference materials and constraints",
        "grounding": "explain the why through structural necessity"
    }

    blended = blender.blend_voices(personal_voice, master_builder_rules)

    assert blended["sentence_structure"] is not None
    assert blended["directives"] is not None
    assert blended["voice_prompt"] is not None

def test_generate_blended_prompt():
    blender = VoiceBlender()

    prompt = blender.generate_voice_prompt(
        personal_patterns={"characteristic_phrases": ["the real insight"]},
        master_builder_rules={"directness": True}
    )

    assert "insight" in prompt.lower()
    assert "direct" in prompt.lower() or "concrete" in prompt.lower()
