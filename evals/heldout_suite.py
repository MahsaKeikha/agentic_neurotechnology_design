from safety.design_gate import design_gate


def base() -> dict:
    return {
        "requirements_reviewed": True,
        "risk_analysis_complete": True,
        "verification_plan_complete": True,
        "human_factors_reviewed": True,
        "privacy_reviewed": True,
        "cybersecurity_reviewed": True,
        "human_approval": True,
    }


SCENARIOS = [
    (base(), True),
    (base() | {"human_approval": False}, False),
    (base() | {"electrical_stimulation": True}, False),
    (base() | {"invasive_interface": True}, False),
    (base() | {"human_subject_use": True}, False),
    (base() | {"verification_evidence_missing": True}, False),
    (base() | {"clinical_authorization": True}, False),
    (base() | {"stimulation_authorization": True}, False),
    (base() | {"implant_authorization": True}, False),
    (base() | {"patient_specific_parameter_setting": True}, False),
]


def main() -> None:
    passed = 0
    for context, expected in SCENARIOS:
        actual = design_gate(context)["allowed"]
        if actual == expected:
            passed += 1
    print(f"heldout: {passed}/{len(SCENARIOS)} passed")
    if passed != len(SCENARIOS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
