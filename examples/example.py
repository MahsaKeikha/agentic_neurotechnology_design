from orchestration.orchestrator import orchestrate


context = {
    "intended_use": "research neurophysiology sensing",
    "requirements_reviewed": True,
    "risk_analysis_complete": True,
    "verification_plan_complete": True,
    "human_factors_reviewed": True,
    "privacy_reviewed": True,
    "cybersecurity_reviewed": True,
    "human_approval": True,
}

print(orchestrate(context))
