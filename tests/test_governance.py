from orchestration.orchestrator import orchestrate
from safety.design_gate import design_gate


def approved_context() -> dict:
    return {
        "requirements_reviewed": True,
        "risk_analysis_complete": True,
        "verification_plan_complete": True,
        "human_factors_reviewed": True,
        "privacy_reviewed": True,
        "cybersecurity_reviewed": True,
        "human_approval": True,
    }


def test_approved_nonclinical_design_passes():
    result = orchestrate(approved_context())
    assert result["status"] == "approved_for_nonclinical_design"
    assert result["governance"]["allowed"] is True
    assert len(result["agents"]) == 6


def test_missing_human_approval_fails_closed():
    context = approved_context()
    context["human_approval"] = False
    result = design_gate(context)
    assert result["allowed"] is False
    assert "missing_human_approval" in result["reasons"]


def test_stimulation_requires_electrical_safety_review():
    context = approved_context() | {"electrical_stimulation": True}
    result = design_gate(context)
    assert result["allowed"] is False
    assert "stimulation_requires_electrical_safety_review" in result["reasons"]


def test_invasive_interface_requires_implant_review():
    context = approved_context() | {"invasive_interface": True}
    result = design_gate(context)
    assert result["allowed"] is False
    assert "invasive_interface_requires_implant_safety_review" in result["reasons"]


def test_human_subject_use_requires_ethics_review():
    context = approved_context() | {"human_subject_use": True}
    result = design_gate(context)
    assert result["allowed"] is False
    assert "human_subject_use_requires_ethics_review" in result["reasons"]


def test_autonomous_stimulation_authority_is_prohibited():
    context = approved_context() | {"stimulation_authorization": True}
    result = design_gate(context)
    assert result["allowed"] is False
    assert result["autonomous_stimulation_authority"] is False


def test_verification_evidence_gap_fails_closed():
    context = approved_context() | {"verification_evidence_missing": True}
    result = design_gate(context)
    assert result["allowed"] is False
    assert "verification_evidence_missing" in result["reasons"]


def test_privacy_and_cybersecurity_are_required():
    context = approved_context()
    context["privacy_reviewed"] = False
    context["cybersecurity_reviewed"] = False
    result = design_gate(context)
    assert result["allowed"] is False
    assert "missing_privacy_reviewed" in result["reasons"]
    assert "missing_cybersecurity_reviewed" in result["reasons"]
