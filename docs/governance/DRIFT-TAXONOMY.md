# Drift Taxonomy

| Drift type | Definition | Example | Default disposition |
|---|---|---|---|
| Scope | Delivery no longer matches authorised scope | Feature added outside baseline | Review |
| Milestone | Forecast/evidence diverges from milestone commitment | Done stories but acceptance missing | Review |
| Benefit | Benefit evidence diverges from target/baseline | Output delivered, outcome unmeasured | Review |
| Risk | Actual exposure differs from accepted position | New risk exceeds appetite | Escalate |
| Dependency | Dependency state threatens authorised plan | External dependency unresolved | Review |
| Cost/Contingency | Consumption crosses configured boundary | Cumulative change uses reserve | Escalate |
| Acceptance Criteria | Criteria change without authorised basis | Definition weakened | Review |
| Authority | Decision made by insufficient authority | PO accepts material scope change | Escalate |
| Delivery Forecast | Forecast diverges from committed milestone | Slip beyond tolerance | Review |
| Governance Documentation | Delivery changed but governance record did not | Baseline not updated | Review |

Classification values:
- none
- isolated_minor_change
- repeated_minor_change
- cumulative_material_change
- unapproved_baseline_change
- governance_review_required
- formal_change_request_required
- insufficient_evidence
