# Risk Model

## Deterministic scoring
Probability and impact are configured values, not LLM guesses.

Starter synthetic scale:
- Probability: 1–5
- Impact: 1–5
- Exposure = Probability × Impact

Portfolio classification:
- 1–4: Low
- 5–9: Moderate
- 10–15: High
- 16–25: Critical

These are synthetic defaults pending owner validation.

Risk governance:
- risk owner must be named;
- acceptance requires authorised risk owner;
- unresolved authority mismatch is a governance breach;
- AI may explain exposure but cannot assign probability/impact or accept risk.
