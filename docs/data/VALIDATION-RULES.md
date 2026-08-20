# Canonical Validation Rules

1. Parse JSON before any business logic.
2. Validate against the active Draft 2020-12 schema.
3. Reject unknown required contract shapes.
4. Reject timestamps that are not valid date-time values.
5. Reject confidence outside 0–1.
6. Reject final outputs missing runId, correlationId, policyVersion or measurementVersion.
7. Preserve missing evidence explicitly rather than inventing values.
8. AI output is invalid until schema validation and evidence-reference checks pass.
9. Human decisions must carry authority role, decision, timestamp and evidence IDs.
10. Public fixtures must remain synthetic and sanitised.
