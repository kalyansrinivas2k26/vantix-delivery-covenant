# Risk Register — Gate 0

Numeric probability/impact scores are intentionally deferred until a deterministic scale is approved.

| ID | Risk | Effect | Current response | Owner role |
|---|---|---|---|---|
| R-001 | Synthetic thresholds mistaken for real organisational policy | misleading governance claims | label/version all defaults | Project Owner |
| R-002 | AI produces unsupported interpretation | unsafe recommendation | schema/evidence validation + human gate | AI Governance Owner |
| R-003 | Delivery evidence is stale or incomplete | false alignment conclusion | freshness and completeness controls | Project Manager |
| R-004 | Authority records are outdated | false approval/violation result | version authority policy and require evidence | PMO/Governance |
| R-005 | Several minor changes escape materiality review | silent baseline drift | cumulative-change engine | Change Authority |
| R-006 | Benefit output is confused with outcome | overstated realised value | baseline/measurement/owner evidence gate | Benefit Owner |
| R-007 | Contradictory indicators are collapsed | false green status | preserve independent dimensions | Project Manager |
| R-008 | Public repository leaks credentials or private data | security/privacy exposure | sanitisation + secret scanning gate | Security Owner |
| R-009 | Schema/policy versions drift from documentation | irreproducible decisions | traceability + CI + checksums | Repository Owner |
| R-010 | Portfolio documentation is interpreted as production proof | unsupported external claim | limitations + claim-evidence matrix | Repository Owner |
