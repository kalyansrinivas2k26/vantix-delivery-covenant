# Control Plan — Gate 0 Starter

This is a design control plan, not evidence of an operating production control system.

| CTQ / risk | Preventive control | Detection control | Reaction | Evidence |
|---|---|---|---|---|
| Unapproved material change | versioned change-authority policy | deterministic materiality/approval check | route to governance review | rule ID + evidence IDs + decision record |
| Authority breach | versioned authority matrix | deterministic role/authority validation | fail closed to required authority | authority result + audit event |
| Unsupported milestone acceptance | milestone evidence contract | completeness and authority checks | prevent accepted state; request evidence | milestone evidence record |
| Unsupported benefit claim | benefit baseline/measurement contract | benefit-state validation | downgrade to pending/inconclusive; route owner review | benefit evidence record |
| Stale evidence | configured freshness windows | freshness calculation | mark limitation / human review | evidence timestamps |
| Invalid AI output | bounded prompt and schema | parse/schema/evidence validation | human review; preserve reason | provider output + validation result |
| Contradictory status | independent status dimensions | contradiction detector | preserve disagreement and escalate if required | contradiction finding |

Control thresholds remain synthetic until explicitly approved.
