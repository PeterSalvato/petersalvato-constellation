# tests/test_guardrails.py
from scripts.guardrails import CaseStudyGuardrails

def test_reject_generic_constraint():
    guardrails = CaseStudyGuardrails()

    draft = {
        "project": "aetherwright",
        "constraint": "Personal system for organizing work",  # Too generic
        "narrative": "I built a system to organize my thoughts"
    }

    result = guardrails.check_constraint_specificity(draft)

    assert not result["passes"]
    assert "too generic" in result["reason"].lower()

def test_accept_specific_constraint():
    guardrails = CaseStudyGuardrails()

    draft = {
        "project": "aetherwright",
        "constraint": "Resists tool fragmentation by using ritual to unify symbolic thinking, documentation, and practice across digital and physical domains",
        "narrative": "..."
    }

    result = guardrails.check_constraint_specificity(draft)

    assert result["passes"]

def test_check_texture_preservation():
    guardrails = CaseStudyGuardrails()

    timeline = [
        {"timestamp": "2025-06-01T10:00:00Z", "content": "Initial realization about ritual"},
        {"timestamp": "2025-07-15T14:00:00Z", "content": "First failure: generic tag system"},
        {"timestamp": "2025-08-20T09:00:00Z", "content": "Pivot to markup language"}
    ]

    result = guardrails.check_timeline_texture(timeline)

    assert result["passes"]
    assert "pivot" in result["findings"].lower()
    assert len(result["key_moments"]) == 3
