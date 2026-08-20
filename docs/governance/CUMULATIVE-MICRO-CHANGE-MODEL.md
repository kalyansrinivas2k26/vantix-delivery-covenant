# Cumulative Micro-Change Model

## Purpose
Detect when several individually minor changes collectively cross a material governance boundary.

## Deterministic evaluation
Within a configured lookback window evaluate:
- count of qualifying minor changes;
- aggregate estimated scope delta;
- contingency consumption;
- acceptance-criteria changes;
- dependency impacts;
- control removals;
- milestone impact.

## Synthetic portfolio defaults
- lookback window: 30 days;
- repeated-minor trigger: 3 events;
- material scope delta: 10%;
- contingency review trigger: 20%.

## Logic
- no qualifying event → `none`
- one minor event below thresholds → `isolated_minor_change`
- repeated events below materiality → `repeated_minor_change`
- aggregate threshold crossed → `cumulative_material_change`
- baseline altered without required approval → `unapproved_baseline_change`
- required evidence missing → `insufficient_evidence`

Crossing a threshold identifies the human authority required; it does not approve the change.
