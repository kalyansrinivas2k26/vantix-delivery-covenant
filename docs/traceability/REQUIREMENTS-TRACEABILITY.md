# Requirements Traceability Matrix — Starter

| Requirement ID | Requirement | Design control | Schema/config | Test status |
|---|---|---|---|---|
| DC-REQ-001 | Detect commitment drift | Drift taxonomy | policy config + drift schema | Fixture prepared |
| DC-REQ-002 | Detect cumulative minor changes | Cumulative-change policy | change-event schema | Fixture prepared |
| DC-REQ-003 | Validate decision authority | Authority matrix | authority-decision schema | Fixture prepared |
| DC-REQ-004 | Require milestone evidence | Milestone evidence gate | milestone-evidence schema | Fixture prepared |
| DC-REQ-005 | Separate output from benefit | Benefit assurance states | benefit-evidence schema | Fixture prepared |
| DC-REQ-006 | Preserve contradictions | Contradiction finding | contradiction schema | Fixture prepared |
| DC-REQ-007 | Fail closed on invalid AI | AI validation boundary | AI-interpretation schema | Negative fixture prepared |
| DC-REQ-008 | Human authority for consequential decisions | Human governance gate | human-decision schema | Contract prepared |
| DC-REQ-009 | Traceable final output | Decision envelope | final-output schema | Valid fixture prepared |
