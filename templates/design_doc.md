# Design Doc: <TITLE>

Status: Draft | Review | Approved | Implemented
Owner: <NAME>
Reviewers: <NAMES>
Date: <YYYY-MM-DD>
Last Updated: <YYYY-MM-DD>

## Summary (TL;DR)
- One paragraph describing the problem and the proposed solution.

## Background
- What problem are we solving?
- Why now?
- Constraints or context from prior work.

## Goals
- Goal 1
- Goal 2

## Non-Goals
- Non-goal 1

## Requirements
### Functional
- Requirement 1

### Non-Functional
- Latency, cost, scalability, reliability, compliance.

## Proposed Solution
- High-level approach and key decisions.
- Architecture sketch (add diagram if needed).

## Detailed Design
- Components and responsibilities.
- Data flow and interfaces (APIs, schemas).
- Storage and compute.
- Dependencies and integration points.

## ML-Specific Design
### Data
- Sources, ownership, and access.
- Volume and refresh cadence.
- Labeling strategy and quality checks.
- Privacy / compliance considerations.

### Features
- Feature definitions and transformations.
- Online vs offline consistency.

### Model
- Model type and rationale.
- Training strategy (batch/online, schedule).
- Hyperparameters and search plan.

### Evaluation
- Metrics and thresholds.
- Baselines and ablations.
- Validation strategy (split, time-based, leakage checks).
- Fairness / bias checks if applicable.

### Experiment Tracking
- Tooling (ClearML by default).
- What gets logged (params, metrics, artifacts).

### Deployment
- Serving pattern (batch, realtime, streaming).
- Rollback strategy and compatibility.

### Monitoring
- Data drift, concept drift, and model decay.
- Operational metrics and alerts.

## Security, Privacy, and Compliance
- Data handling and retention.
- PII/PHI considerations.
- Access controls.

## Test Plan
- Unit tests
- Integration tests
- Offline evaluation tests
- Shadow or canary tests

## Rollout Plan
- Phased rollout steps.
- Success metrics and guardrails.

## Risks and Mitigations
- Risk 1 -> Mitigation

## Alternatives Considered
- Option A
- Option B

## Milestones
- Milestone 1
- Milestone 2

## Open Questions
- Question 1
