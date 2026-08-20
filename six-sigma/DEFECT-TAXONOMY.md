# Defect Taxonomy — Candidate Gate 0 Definitions

These are candidate operational categories for the portfolio build. They are not organisation-specific thresholds.

| Defect ID | Defect | Unit | Trigger concept | Current status |
|---|---|---|---|---|
| DEF-001 | Material change implemented before required approval | material change | configured materiality + missing prior approval | Candidate |
| DEF-002 | Consequential decision made by insufficient authority | governance decision | active authority policy mismatch | Candidate |
| DEF-003 | Milestone accepted with incomplete required evidence | milestone assessment | accepted state + failed evidence gate | Candidate |
| DEF-004 | Benefit claimed achieved without required measured evidence | benefit claim | achieved/sustained state + evidence deficiency | Candidate |
| DEF-005 | Material cumulative change not escalated | configured change window | aggregate threshold crossed without route | Candidate |
| DEF-006 | Stale evidence used without explicit limitation | decision assessment | freshness policy exceeded | Candidate |
| DEF-007 | Story or feature cannot be traced to an approved outcome | delivery item | missing outcome linkage | Candidate |
| DEF-008 | Contradictory status suppressed or collapsed | reconciliation run | conflicting indicators replaced by single status | Candidate |

Before quantitative use, each defect requires an approved operational definition, sampling boundary and measurement-system check.
