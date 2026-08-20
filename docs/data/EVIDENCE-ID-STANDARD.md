# Evidence Identifier Standard

## Purpose
Allow every recommendation, finding and human decision to trace back to concrete evidence.

## Format
Use readable synthetic IDs in the portfolio build:

`<TYPE>-<NNN>`

Examples:
- `EVID-001`
- `COMMIT-001`
- `CHG-001`
- `DEC-001`
- `MS-001`
- `BEN-001`
- `RISK-001`
- `DRIFT-001`
- `CONTRA-001`
- `RUN-001`
- `CORR-001`

## Rules
- IDs are immutable once published in evidence.
- IDs are not reused for different business objects.
- Public fixtures use synthetic IDs only.
- Source-system native identifiers may be stored later as mapped source references but must not replace canonical IDs.
- Evidence IDs must never contain credentials, tokens or private environment identifiers.
