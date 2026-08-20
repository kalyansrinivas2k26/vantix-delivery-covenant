# Repository Governance

## Decision principles
1. Evidence over assertion.
2. Deterministic controls before AI for consequential logic.
3. Human authority for consequential governance decisions.
4. Version changes that alter policy, measurement or schemas.
5. Synthetic and live evidence remain separated.
6. Release maturity is evidence-gated.

## Change classes
- **Documentation-only:** wording/format with no behavioural claim change.
- **Control change:** policy, authority, measurement or deterministic behaviour.
- **Contract change:** schema or decision-envelope change.
- **AI change:** prompt, model interface, confidence or validation change.
- **Release change:** CI, sanitisation, evidence or maturity-tier change.

Control, contract and AI changes require traceability and regression impact review.
