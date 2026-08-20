# Benefit Evidence Rules

## Principle
Outputs are not outcomes.

Every benefit definition requires:
- benefit ID;
- benefit owner;
- baseline;
- target;
- measurement method;
- source;
- measurement cadence;
- expected realisation window;
- acceptance authority;
- sustainment check.

States:
`planned`, `baseline_missing`, `measurement_pending`, `early_signal`, `partially_evidenced`, `achieved`, `not_achieved`, `inconclusive`, `deteriorated`, `sustained`, `relapsed`.

Restrictions:
- `achieved` requires measured evidence against defined baseline/target logic;
- `sustained` requires later-period evidence;
- task completion alone cannot set `achieved`;
- missing baseline routes to `baseline_missing`;
- contradictory/insufficient measurement routes to `inconclusive`.
