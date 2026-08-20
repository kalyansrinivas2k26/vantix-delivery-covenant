# Gate 2 — Canonical Data & Schemas

## Objective
Define stable, provider-neutral contracts for delivery evidence, governance commitments, changes, authority decisions, milestones, benefits, risks, contradictions, drift findings, AI interpretations, human decisions, audit events and the final Delivery Covenant Decision Envelope.

## Design principles
- provider-neutral canonical model;
- synthetic public fixtures only;
- stable evidence identifiers;
- explicit schema versioning;
- explicit policy and measurement versioning;
- additional properties rejected in public contracts unless intentionally allowed;
- timestamps use RFC 3339 date-time strings;
- consequential outputs preserve evidence IDs;
- schema validation is performed by a real Draft 2020-12 validator.

## Gate 2 outputs
- canonical data dictionary;
- evidence identifier standard;
- versioning standard;
- synthetic project dataset;
- positive and negative fixtures;
- schema coverage matrix;
- validation rules;
- Gate 2 acceptance checklist.

## Guardrail
The canonical model must not encode Salesforce-only assumptions. Salesforce may map into this model later as one evidence provider.
