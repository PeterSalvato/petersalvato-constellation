# tests/test_prose_generator.py
from scripts.prose_generator import ProseGenerator

def test_generate_prose_from_skeleton():
    generator = ProseGenerator()

    skeleton = {
        "project": "savepoint-protocol",
        "constraint": "Capture semantic turning points where thinking shifts",
        "arc": [
            {
                "type": "genesis",
                "timestamp": "2024-09-30T10:00:00Z",
                "snippet": "I need a way to mark where my thinking changed",
                "platform": "claude"
            },
            {
                "type": "problem",
                "timestamp": "2024-10-05T14:30:00Z",
                "snippet": "Tagging systems don't capture the shift",
                "platform": "claude"
            },
            {
                "type": "pivot",
                "timestamp": "2024-10-15T09:00:00Z",
                "snippet": "Markup language preserves the moment",
                "platform": "claude"
            }
        ]
    }

    voice_prompt = "Your characteristic voice..."

    prose = generator.generate_prose(skeleton, voice_prompt)

    assert prose is not None
    assert len(prose) > 200
    assert "savepoint" in prose.lower() or "mark" in prose.lower()

def test_validate_skeleton_fidelity():
    generator = ProseGenerator()

    skeleton = {
        "constraint": "Capture thinking shifts",
        "arc": [{"snippet": "mark where thinking changed"}]
    }

    prose = "Built a system to capture semantic turning points..."

    validation = generator.validate_fidelity(prose, skeleton)

    assert validation["fidelity_score"] > 0
    assert "coherent" in validation or validation["issues"] is not None
