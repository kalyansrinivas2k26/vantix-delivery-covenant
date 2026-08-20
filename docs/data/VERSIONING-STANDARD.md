# Versioning Standard

## schemaVersion
Changes when the machine-readable contract changes.

## policyVersion
Changes when deterministic governance behaviour or thresholds change.

## measurementVersion
Changes when operational definitions, numerator/denominator logic or CTQ calculations change.

## promptVersion
Changes when bounded AI instructions materially change.

## Compatibility
- additive optional fields may be backward compatible;
- new required fields are breaking changes;
- enum removals/renames are breaking changes;
- semantic changes to an existing field are breaking changes even if JSON shape is unchanged.

Every final output must record the active schema, policy and measurement versions.
