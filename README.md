# Agentic Neurotechnology Design

**F66 | L3 Gold Standard | v1.0**

A standalone multi-agent engineering workflow for neurotechnology requirements, sensing architecture, signal-pipeline design, human factors, risk analysis, verification planning, and qualified human review.

This repository supports engineering and research workflows. It does not authorize clinical use, stimulation, implantation, treatment, or patient-specific parameter setting, and it does not replace regulatory, safety, ethics, or clinical review.

## Core agents

- [`requirements_agent.py`](AGENTS/requirements_agent.py)
- [`sensing_architecture_agent.py`](AGENTS/sensing_architecture_agent.py)
- [`signal_pipeline_agent.py`](AGENTS/signal_pipeline_agent.py)
- [`human_factors_agent.py`](AGENTS/human_factors_agent.py)
- [`risk_verification_agent.py`](AGENTS/risk_verification_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Gold-standard governance

The design gate fails closed unless requirements, risk analysis, verification planning, human factors, privacy, cybersecurity, and qualified human approval are complete. Invasive interfaces require implant-safety review. Electrical stimulation requires electrical-safety review. Human-subject use requires ethics review. Verification evidence gaps block approval.

Autonomous clinical authorization, stimulation authorization, implant authorization, treatment decisions, and patient-specific parameter setting are prohibited.

## Verification

CI runs on Python 3.10, 3.11, and 3.12 and includes correctness-focused Ruff checks, pytest, a held-out governance suite, example execution, and smoke execution.

The held-out suite covers approved nonclinical design plus missing approval, electrical stimulation, invasive interfaces, human-subject use, verification gaps, clinical authorization, stimulation authorization, implant authorization, and patient-specific parameter setting.

## Architecture

[`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```
