# tests/test_voice_extractor.py
from scripts.voice_extractor import VoiceExtractor

def test_extract_voice_patterns():
    extractor = VoiceExtractor()

    sample_conversations = [
        {
            "content": "I need a way to mark where my thinking changed, not just what I thought",
            "platform": "claude"
        },
        {
            "content": "This pattern shows up everywhere: when you own the entire system end-to-end, coherence survives.",
            "platform": "claude"
        }
    ]

    patterns = extractor.extract_patterns(sample_conversations)

    assert patterns["sentence_structure"] is not None
    assert patterns["vocabulary"] is not None
    assert patterns["metaphors"] is not None
    assert patterns["pacing"] is not None

def test_identify_characteristic_phrases():
    extractor = VoiceExtractor()

    sample_conversations = [
        {"content": "The real insight is that..."},
        {"content": "What actually matters is..."},
        {"content": "The tension is between..."}
    ]

    phrases = extractor.identify_characteristic_phrases(sample_conversations)

    assert "insight" in str(phrases).lower()
