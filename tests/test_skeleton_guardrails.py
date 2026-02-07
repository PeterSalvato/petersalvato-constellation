from scripts.skeleton_guardrails import SkeletonGuardrails

def test_reject_flat_constraint():
    guardrails = SkeletonGuardrails()

    skeleton = {
        "project": "test",
        "constraint": "Personal system for work",
        "arc": [],
        "texture_score": 0.1
    }

    result = guardrails.validate(skeleton)

    assert not result["passes"]
    assert "generic" in result["issues"][0].lower()

def test_reject_low_texture():
    guardrails = SkeletonGuardrails()

    skeleton = {
        "project": "test",
        "constraint": "A specific and detailed constraint that provides meaningful context for the project",
        "arc": [{"type": "genesis"}],
        "texture_score": 0.05
    }

    result = guardrails.validate(skeleton)

    assert not result["passes"]
    assert "texture" in result["issues"][0].lower()

def test_accept_good_skeleton():
    guardrails = SkeletonGuardrails()

    skeleton = {
        "project": "savepoint-protocol",
        "constraint": "Capture semantic turning points where thinking shifts and meaning clicks",
        "arc": [
            {"type": "genesis"},
            {"type": "problem"},
            {"type": "pivot"},
            {"type": "validation"}
        ],
        "texture_score": 0.75
    }

    result = guardrails.validate(skeleton)

    assert result["passes"]
