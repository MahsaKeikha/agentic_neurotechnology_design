from AGENTS.human_factors_agent import HumanFactorsAgent
from AGENTS.human_review_agent import HumanReviewAgent
from AGENTS.requirements_agent import RequirementsAgent
from AGENTS.risk_verification_agent import RiskVerificationAgent
from AGENTS.sensing_architecture_agent import SensingArchitectureAgent
from AGENTS.signal_pipeline_agent import SignalPipelineAgent
from safety.design_gate import design_gate

AGENTS = [
    RequirementsAgent(),
    SensingArchitectureAgent(),
    SignalPipelineAgent(),
    HumanFactorsAgent(),
    RiskVerificationAgent(),
    HumanReviewAgent(),
]


def orchestrate(context: dict) -> dict:
    """Run specialists and apply fail-closed neurotechnology design governance."""
    specialist_results = [agent.run(context) for agent in AGENTS]
    gate = design_gate(context)
    return {
        "agents": specialist_results,
        "governance": gate,
        "status": "approved_for_nonclinical_design" if gate["allowed"] else "review_required",
    }
