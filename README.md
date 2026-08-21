# Agentic Neurotechnology Design

F66 in the Agentic AI Library.

A standalone multi-agent engineering workflow for neurotechnology requirements, sensing architecture, signal pipeline design, human factors, risk analysis, verification planning, and human review.

This repository supports engineering and research workflows. It does not authorize clinical use or replace regulatory, safety, or clinical review.

## Core agents

- [`requirements_agent.py`](AGENTS/requirements_agent.py)
- [`sensing_architecture_agent.py`](AGENTS/sensing_architecture_agent.py)
- [`signal_pipeline_agent.py`](AGENTS/signal_pipeline_agent.py)
- [`human_factors_agent.py`](AGENTS/human_factors_agent.py)
- [`risk_verification_agent.py`](AGENTS/risk_verification_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Architecture

[`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```
