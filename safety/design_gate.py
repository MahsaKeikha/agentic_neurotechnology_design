REQUIRED_REVIEWS = (
    "requirements_reviewed",
    "risk_analysis_complete",
    "verification_plan_complete",
    "human_factors_reviewed",
    "privacy_reviewed",
    "cybersecurity_reviewed",
    "human_approval",
)

PROHIBITED_AUTONOMOUS_ACTIONS = (
    "clinical_authorization",
    "stimulation_authorization",
    "implant_authorization",
    "treatment_decision",
    "patient_specific_parameter_setting",
)


def design_gate(context: dict) -> dict:
    """Fail closed for consequential neurotechnology design or human-use decisions."""
    reasons: list[str] = []

    for key in REQUIRED_REVIEWS:
        if not context.get(key, False):
            reasons.append(f"missing_{key}")

    for key in PROHIBITED_AUTONOMOUS_ACTIONS:
        if context.get(key, False):
            reasons.append(f"autonomous_{key}_not_permitted")

    if context.get("invasive_interface", False) and not context.get(
        "implant_safety_reviewed", False
    ):
        reasons.append("invasive_interface_requires_implant_safety_review")

    if context.get("electrical_stimulation", False) and not context.get(
        "electrical_safety_reviewed", False
    ):
        reasons.append("stimulation_requires_electrical_safety_review")

    if context.get("human_subject_use", False) and not context.get(
        "ethics_reviewed", False
    ):
        reasons.append("human_subject_use_requires_ethics_review")

    if context.get("verification_evidence_missing", False):
        reasons.append("verification_evidence_missing")

    return {
        "allowed": not reasons,
        "requires_human_review": True,
        "reasons": reasons,
        "autonomous_clinical_authority": False,
        "autonomous_stimulation_authority": False,
        "autonomous_implant_authority": False,
    }
