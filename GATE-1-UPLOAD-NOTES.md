# Gate 1 Upload Notes — Corrected Package

Upload all files in this ZIP to the existing repository root while preserving the paths.

Commit:
`feat: add Delivery Covenant Gate 1 governance design`

Important:
- Do not upload any earlier Gate 1 ZIP or CI-fix ZIP.
- Do not delete Gate 0 files.
- This package replaces the previous whole-repository checksum model with an explicit release-controlled checksum scope.
- Existing README, RELEASE_NOTES, START_HERE, GitHub metadata and other mutable repository files are intentionally outside the Gate 1 checksum scope.

After upload:
1. Commit.
2. Wait for `CI - Delivery Covenant`.
3. Confirm it is green.
4. Do not start n8n yet.
