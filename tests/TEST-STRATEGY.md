# Test Strategy

## Deterministic
- positive cases
- negative cases
- threshold boundaries
- cumulative-change windows
- authority mismatch
- stale evidence
- duplicate evidence
- missing IDs
- schema validation

## Workflow integration — Gate 5+
- routing
- error workflow
- retry
- timeout
- idempotency
- persistence
- audit recording

## Live-provider — Gate 6+
- valid structured response
- malformed output
- parseable schema-invalid output
- low confidence
- timeout
- contradiction challenge
- unsupported recommendation
- human review route

Current repository tests validate contracts and repository integrity only. They do not claim n8n or provider execution.
