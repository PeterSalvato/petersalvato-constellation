# tests/test_prose_guardrails.py
from scripts.prose_guardrails import ProseGuardrails

def test_reject_generic_prose():
    guardrails = ProseGuardrails()

    prose = "I built a system to help organize work better."

    result = guardrails.validate(prose)

    assert not result["passes"]
    assert "generic" in result["issues"][0].lower()

def test_reject_marketing_language():
    guardrails = ProseGuardrails()

    prose = "This innovative solution empowers teams to synergize their workflows."

    result = guardrails.validate(prose)

    assert not result["passes"]
    assert any("marketing" in issue.lower() for issue in result["issues"])

def test_accept_grounded_prose():
    guardrails = ProseGuardrails()

    prose = """Built a markup language to capture semantic turning points.

The problem: tagging systems don't preserve the moment where thinking shifted.
They capture what you thought, not where you realized it.

The solution: a format that marks inflection points. When understanding clicks,
the system captures that moment, not just the outcome. This means later, you can
retrace the thinking, not just the data."""

    result = guardrails.validate(prose)

    assert result["passes"]
