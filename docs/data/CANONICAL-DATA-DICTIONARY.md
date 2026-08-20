# Canonical Data Dictionary

## Common identifiers

| Field | Meaning | Rule |
|---|---|---|
| schemaVersion | Contract version | semantic version string |
| runId | One execution | stable unique ID |
| correlationId | Cross-step correlation | stable across one end-to-end case |
| projectId | Project/programme identifier | provider-neutral |
| evidenceId | Source evidence identifier | immutable within evidence source |
| observedAt | Evidence observation time | RFC 3339 date-time |
| policyVersion | Deterministic policy version | explicit |
| measurementVersion | Measurement definition version | explicit |

## Delivery evidence
Represents observed Agile execution, never the approved governance baseline.

Core attributes:
projectId, storyId, epicId, sprintId, sprintGoal, acceptanceCriteria, definitionOfReady, definitionOfDone, status, linkedOutcomeId, blockers, defects, rework, evidenceId, sourceSystem, observedAt, evidenceFreshnessDays.

## Governance commitment
Represents authorised project intent.

Core attributes:
commitmentId, projectId, governanceVersion, approvedOutcome, scopeInclusions, scopeExclusions, milestoneIds, riskIds, decisionAuthorityIds, benefitIds, approvedAt, evidenceId.

## Change event
Represents one observed change that may contribute to individual or cumulative drift.

Core attributes:
changeId, projectId, observedAt, changeType, description, materiality, estimatedDeltaPercent, evidenceIds.

## Authority decision
Represents an approval or decision requiring authority validation.

Core attributes:
decisionId, decisionType, requiredAuthority, recordedDecisionMakerRole, authorityStatus, evidenceIds, approvedAt.

## Milestone evidence
Represents evidence required for milestone acceptance.

## Benefit evidence
Represents baseline, target and measured-outcome evidence separately from output completion.

## Contradiction finding
Preserves conflicting indicators rather than collapsing them into one RAG status.

## Drift finding
Represents deterministic divergence between delivery reality and governance commitment.

## AI interpretation
Untrusted bounded interpretation that requires schema and evidence validation.

## Human decision
Records the consequential human disposition.

## Audit event
Records traceable lifecycle events.

## Final decision envelope
The machine-readable end-state contract aggregating statuses, evidence, required authority, limitations and human decision state.
