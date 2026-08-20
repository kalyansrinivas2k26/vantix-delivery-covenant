# Benefit Evidence Rules

## Principle
Outputs are not outcomes.

Required benefit definition:
- benefitId
- benefitOwner
- baseline
- target
- measurement method
- source
- cadence
- expected realisation window
- acceptance authority
- sustainment check

States:
planned, baseline_missing, measurement_pending, early_signal, partially_evidenced, achieved, not_achieved, inconclusive, deteriorated, sustained, relapsed.

Deterministic restrictions:
- `achieved` requires baseline/target logic and measured evidence;
- `sustained` requires a later measurement window;
- task completion alone cannot set `achieved`;
- missing baseline routes to `baseline_missing`;
- insufficient or contradictory measurements route to `inconclusive`.
