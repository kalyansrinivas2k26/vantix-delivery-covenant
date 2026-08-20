# Cumulative Micro-Change Model

## Purpose
Prevent individually minor changes from escaping governance when their aggregate effect becomes material.

## Deterministic evaluation
Within a configured lookback window, evaluate:
- count of minor changes;
- aggregate estimated scope delta;
- contingency consumption;
- acceptance-criteria changes;
- dependency impact;
- control removals;
- milestone impact.

## Starter synthetic defaults
- lookback window: 30 days;
- repeated-minor trigger: 3 events;
- material scope delta: 10%;
- contingency review trigger: 20%.

These remain portfolio assumptions until owner validation.

## Classification logic
1. No qualifying event → `none`
2. One minor event below thresholds → `isolated_minor_change`
3. Repeated qualifying events below materiality → `repeated_minor_change`
4. Aggregate threshold crossed → `cumulative_material_change`
5. Baseline altered without required approval → `unapproved_baseline_change`
6. Required evidence missing → `insufficient_evidence`

Crossing a threshold identifies the human authority required; it does not approve the change.
