# ADR-001 — Deterministic Controls Before AI

**Status:** Accepted

## Context
The system evaluates governance-sensitive evidence such as decision authority, material change and milestone acceptance.

## Decision
Deterministic rules execute before optional AI interpretation. AI output is treated as untrusted and must pass parsing, schema, evidence and authority-bound validation.

## Consequences
- stronger reproducibility;
- clearer auditability;
- more explicit policy versioning;
- additional configuration and test maintenance;
- AI can explain or challenge but cannot become the source of governance truth.
