# F66 Agentic Neurotechnology Design

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A governed six-agent reference architecture for neurotechnology engineering across requirements, sensing architecture, signal-pipeline design, human factors, risk analysis, verification planning, and qualified human review.

F66 is intended as a reusable engineering reference for teams designing systems that interact with neural or neurophysiological signals. It separates design reasoning from deterministic engineering evidence and keeps consequential clinical, stimulation, implant, ethics, and release authority behind explicit human review.

This repository supports engineering and research workflows only. It does not authorize clinical use, prescribe or deliver stimulation, authorize implantation, determine treatment, select patient-specific parameters, or replace regulatory, safety, ethics, or clinical professionals.

## Multi-agent architecture

```text
Intended Use and Requirements
            |
            v
   Sensing Architecture
            |
            v
      Signal Pipeline
            |
            v
       Human Factors
            |
            v
   Risk and Verification
            |
            v
 Qualified Human Review
```

| Agent | Responsibility | Core question |
|---|---|---|
| Requirements Agent | Intended use, users, environment, claims, constraints, and traceability | Is the design problem clearly defined and testable? |
| Sensing Architecture Agent | Neural interfaces, sensors, electrodes, channels, references, and acquisition hardware | Can the intended signals be acquired safely and with sufficient fidelity? |
| Signal Pipeline Agent | Sampling, filtering, synchronization, preprocessing, features, latency, and integrity | Is the signal path technically valid and reproducible? |
| Human Factors Agent | Setup, comfort, usability, accessibility, workflow, and use-related risk | Can intended users interact with the system safely and reliably? |
| Risk Verification Agent | Hazards, controls, cybersecurity, verification evidence, and unresolved gaps | Are risks and requirements linked to objective evidence? |
| Human Review Agent | Engineering, safety, ethics, clinical, and regulatory authority boundary | Has an appropriately qualified person reviewed the design? |

## Repository structure

```text
AGENTS/
SKILLS/
TOOLS/
├── requirements_matrix_tool.py
├── interface_inventory_tool.py
├── risk_register_tool.py
├── verification_matrix_tool.py
└── provenance_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/tests.yml
run.py
README.md
```

The architecture separates reasoning from deterministic engineering artifacts so that requirements, interfaces, risks, tests, and approvals remain traceable.

## Requirements and intended use

A neurotechnology design should begin with an explicit engineering contract. Relevant fields include intended use, intended user, use environment, research versus clinical context, invasive versus non-invasive interface, sensed modalities, output modalities, performance targets, safety constraints, latency, privacy, cybersecurity, interoperability, power, environmental constraints, and verification methods.

`TOOLS/requirements_matrix_tool.py` provides the reference traceability layer.

A useful chain is:

```text
user need
   -> system requirement
   -> interface or design element
   -> risk control where applicable
   -> verification evidence
```

Missing requirements or unsupported claims should remain visible rather than being inferred into completeness.

## Sensing architecture

The Sensing Architecture Agent reviews how biological signals enter the system. Depending on the application, interfaces can include EEG, EMG, EOG, ECG, peripheral neural signals, optical sensing, inertial sensing, or other physiological channels.

Relevant engineering considerations include electrode or sensor type, placement, contact quality, reference strategy, channel count, input range, noise floor, common-mode rejection, impedance assumptions, ADC resolution, sampling rate, anti-aliasing, electrical isolation, synchronization, connector safety, and hardware revision control.

`TOOLS/interface_inventory_tool.py` records interfaces and assumptions.

### Invasive versus non-invasive systems

Non-invasive systems still require safety and usability review. Invasive interfaces require substantially stronger evidence for biocompatibility, sterility, implantation, long-term reliability, infection risk, tissue interaction, explant/revision considerations, and clinical oversight.

F66 does not authorize implant design for human use. Any invasive human-subject application requires qualified engineering, clinical, ethics, regulatory, and institutional review.

## Signal pipeline

The Signal Pipeline Agent documents how raw measurements become analysis-ready signals or features.

A reproducible pipeline should state:

- sampling frequency
- units and calibration
- referencing or montage
- synchronization method
- filtering parameters
- notch filtering where applicable
- resampling
- artifact handling
- epoching or segmentation
- normalization
- feature definitions
- rejected-channel or rejected-window criteria
- software and configuration versions

Changing preprocessing can materially change downstream results. Filter settings and artifact corrections should therefore be versioned rather than hidden behind generic labels such as "cleaned data."

## Signal integrity and timing

Neurotechnology systems may depend on small amplitudes and precise timing. Reviews should consider noise, saturation, clipping, drift, packet loss, clock drift, dropped samples, aliasing, channel swaps, synchronization errors, wireless interruption, buffering, and timestamp provenance.

For closed-loop research systems, latency should be decomposed across acquisition, buffering, processing, decision logic, communications, and output. An average latency alone may hide unsafe or scientifically invalid worst-case behavior.

## Stimulation and closed-loop boundaries

Electrical, magnetic, acoustic, optical, mechanical, or other stimulation introduces additional safety responsibilities.

A stimulation design review can identify requirements for output limits, waveform constraints, charge or energy limits, duty cycle, interlocks, emergency stop behavior, timing, isolation, hardware fault handling, and verification. However, F66 must not independently determine safe human stimulation parameters or authorize stimulation.

Patient-specific stimulation settings, treatment decisions, implant activation, and real-world clinical control remain outside autonomous authority.

## Human factors

The Human Factors Agent reviews the relationship between the user, device, task, and environment.

Relevant concerns include donning and doffing, electrode placement, setup errors, user training, comfort, skin interaction, cable management, accessibility, alarm interpretation, feedback design, cognitive burden, maintenance, cleaning, charging, and foreseeable misuse.

Human-factors findings should feed back into requirements and the risk register.

## Risk management

`TOOLS/risk_register_tool.py` provides the structured risk layer.

A useful risk record includes:

```text
risk_id
hazard
hazardous_situation
potential_harm
initial_risk
risk_control
implementation_reference
verification_reference
residual_risk
owner
status
```

Example categories include electrical hazards, thermal hazards, mechanical hazards, skin injury, incorrect electrode placement, signal corruption, false feedback, unsafe stimulation, loss of communication, software failure, cybersecurity compromise, privacy loss, and use error.

The repository supports risk organization, not autonomous acceptance of residual risk.

## Verification planning

`TOOLS/verification_matrix_tool.py` links requirements and risk controls to objective evidence.

Verification can include inspection, analysis, bench testing, simulation, software testing, hardware testing, signal-injection testing, fault injection, latency testing, environmental testing, usability evaluation, and other justified methods.

Acceptance criteria should be explicit. A requirement is not verified because an agent says it appears reasonable.

## Cybersecurity and privacy

Connected neurotechnology can expose exceptionally sensitive physiological and behavioral data. Production systems should consider authenticated identities, authorization, least privilege, encrypted communications, key management, secure updates, dependency provenance, audit logging, data minimization, retention, de-identification where appropriate, and protections against unauthorized control.

Cybersecurity findings that can alter device behavior, stimulation, signal integrity, availability, or privacy should be treated as engineering risks rather than isolated IT findings.

## Human-subject research boundary

Use with human participants may require institutional ethics review, informed consent, protocol controls, adverse-event processes, privacy protections, qualified supervision, and additional device-specific regulatory oversight.

F66 may organize requirements and open questions, but it does not determine that a study is exempt, approve a protocol, consent a participant, or authorize human use.

## Provenance and shared state

`TOOLS/provenance_tool.py`, `memory/`, and `state/` preserve the evidence chain across agents.

Useful provenance includes hardware revision, firmware/software version, sensor configuration, acquisition settings, preprocessing version, dataset identifier, calibration state, risk-file version, verification protocol, verification result, and reviewer status.

Results from one configuration should not silently be reused as evidence for a materially different configuration.

## Fail-closed governance

The design gate blocks approval when required evidence is absent or unresolved. Examples include:

- intended use incomplete
- requirements incomplete
- interface definition incomplete
- sensing architecture unverified
- signal pipeline undocumented
- risk analysis incomplete
- risk control verification missing
- human-factors review missing
- privacy review missing
- cybersecurity review missing
- invasive interface without implant-safety review
- electrical stimulation without electrical-safety review
- human-subject use without ethics review
- verification evidence gap
- unresolved critical risk
- patient-specific parameter request
- clinical authorization request
- stimulation or implant authorization request
- qualified human approval missing

Human approval cannot convert missing safety evidence into verified evidence.

## Authority boundaries

F66 must not autonomously:

- diagnose neurological disease
- prescribe treatment
- determine clinical efficacy
- set patient-specific stimulation parameters
- trigger human stimulation
- authorize implantation
- approve human-subject use
- accept residual clinical risk
- approve regulatory claims
- authorize commercial or clinical release

Those decisions remain with qualified and authorized humans and applicable institutional processes.

## End-to-end reference workflow

1. Define intended use, users, environment, and system boundaries.
2. Capture requirements and claims.
3. Define sensing interfaces and hardware assumptions.
4. Document the complete signal pipeline.
5. Review timing, integrity, and failure behavior.
6. Review human factors and foreseeable use errors.
7. Identify hazards and assign risk controls.
8. Review privacy and cybersecurity.
9. Build requirement-to-verification traceability.
10. Confirm ethics, implant, stimulation, or clinical reviews where applicable.
11. Consolidate unresolved risks and evidence gaps.
12. Apply the fail-closed design gate.
13. Require qualified human approval.

## Evaluation and held-out testing

The repository includes `evals/`, `benchmarks/`, examples, tests, and CI. Evaluation should measure governance behavior rather than prose quality alone.

Useful dimensions include requirements-gap detection, interface-gap detection, undocumented preprocessing, missing verification, unsafe stimulation authority requests, invasive-interface escalation, ethics-review enforcement, privacy and cybersecurity review, unresolved-risk propagation, and human-gate enforcement.

The held-out suite specifically includes nonclinical approval cases and failure cases for missing approval, electrical stimulation, invasive interfaces, human-subject use, verification gaps, clinical authorization, stimulation authorization, implant authorization, and patient-specific parameter setting.

## Reproduce the reference implementation

```bash
python -m pip install -e '.[dev]'
ruff check .
python -m pytest -q
python evals/heldout_suite.py
python examples/example.py
python run.py
```

CI runs across Python 3.10, 3.11, and 3.12.

## Explicit failure states

```text
REQUIREMENTS INCOMPLETE
INTERFACE DEFINITION INCOMPLETE
SIGNAL PIPELINE UNVERIFIED
RISK ANALYSIS INCOMPLETE
RISK CONTROL UNVERIFIED
HUMAN FACTORS REVIEW REQUIRED
PRIVACY REVIEW REQUIRED
CYBERSECURITY REVIEW REQUIRED
IMPLANT SAFETY REVIEW REQUIRED
ELECTRICAL SAFETY REVIEW REQUIRED
ETHICS REVIEW REQUIRED
VERIFICATION EVIDENCE MISSING
PATIENT-SPECIFIC PARAMETER REQUEST BLOCKED
CLINICAL AUTHORIZATION BLOCKED
STIMULATION AUTHORIZATION BLOCKED
IMPLANT AUTHORIZATION BLOCKED
QUALIFIED HUMAN APPROVAL REQUIRED
```

The system should never fabricate a test result, safety limit, ethics approval, clinical authorization, implant approval, stimulation approval, or reviewer sign-off.

## Extending F66

Common extensions include EEG and biosignal hardware adapters, synchronized multimodal acquisition, wearable systems, wireless sensors, edge processing, BCI pipelines, digital biomarkers, neurofeedback research, stimulation-device research interfaces, hardware-in-loop testing, signal simulators, calibration systems, requirements platforms, eQMS integrations, cybersecurity tooling, and research data platforms.

Extensions should preserve provenance, deterministic validation, fail-closed gates, and human authority.

## L3 Gold Standard candidate

The L3 designation describes the engineering maturity of this reference architecture: specialist agents, deterministic tools, traceable evidence, explicit safety boundaries, held-out governance testing, observability, CI, and mandatory human approval.

It is not medical-device certification, clinical validation, ethics approval, regulatory clearance, proof of treatment efficacy, or authorization for human stimulation or implantation.

## Design principles

1. Define intended use before designing the signal chain.
2. Treat neural interfaces as explicit safety and data-quality boundaries.
3. Make every preprocessing step reproducible.
4. Preserve timing and signal provenance.
5. Integrate human factors, privacy, and cybersecurity early.
6. Trace risks to controls and controls to verification.
7. Distinguish research evidence from clinical evidence.
8. Fail closed when consequential evidence is missing.
9. Never infer authorization from technical feasibility.
10. Keep clinical, stimulation, implant, ethics, and release authority with qualified humans.

## Responsible use

Use F66 as a neurotechnology engineering and multi-agent systems reference. Validate sensing hardware, signal processing, risks, cybersecurity, privacy, usability, verification evidence, ethics requirements, and regulatory obligations against the actual system before any real-world deployment. Final safety, human-subject, stimulation, implant, clinical, and release decisions remain with qualified and authorized professionals.