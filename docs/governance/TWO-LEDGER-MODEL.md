# Two-Ledger Operating Model

## Ledger 1 — Delivery Reality Ledger
Represents observed Agile execution.

Core fields:
- projectId
- epicId
- storyId
- sprintId
- sprintGoal
- acceptanceCriteria
- Definition of Ready / Definition of Done
- status
- forecast
- carryover
- blockers
- defects
- rework
- dependencies
- release evidence
- linkedOutcomeId
- evidenceId
- source
- observedAt
- freshness

## Ledger 2 — Governance Commitment Ledger
Represents approved project intent.

Core fields:
- projectId
- governanceVersion
- approvedOutcome
- scope inclusions / exclusions
- milestone commitments
- acceptance criteria
- contingency rules
- RAID
- decision authorities
- benefit baselines / targets / owners
- closure criteria
- approval evidence
- evidenceId
- approvedAt

## Reconciliation principle
The Delivery Reality Ledger never overwrites the Governance Commitment Ledger. Differences become explicit findings.
