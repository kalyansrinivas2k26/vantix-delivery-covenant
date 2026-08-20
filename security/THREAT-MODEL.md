# Threat Model — Starter

## Assets
- governance commitments;
- delivery evidence;
- authority records;
- benefit evidence;
- decision envelopes;
- credentials;
- audit trail.

## Trust boundaries
1. external source systems → ingestion;
2. canonical evidence store → deterministic control engine;
3. deterministic results → AI provider;
4. AI output → validation boundary;
5. validated recommendation → human governance gate;
6. internal evidence → public portfolio release.

## Key threats and controls
- **Prompt injection:** evidence-bound prompts; treat source text as data; do not grant tool authority to model.
- **Malformed/hostile AI output:** strict parsing and schema validation.
- **Unsupported recommendation:** evidence-ID and policy-rule checks.
- **Credential leakage:** externalise credentials; public sanitisation gate; secret scan.
- **Replay/duplicate execution:** correlation IDs and idempotency.
- **Authority spoofing:** validate recorded decision-maker against versioned authority policy.
- **Evidence tampering:** evidence IDs/hashes and release checksum manifest.
- **Stale evidence:** freshness classification and explicit limitation.
- **Public-data leakage:** synthetic fixtures only and release sanitisation.
