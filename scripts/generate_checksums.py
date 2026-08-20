from pathlib import Path
import hashlib, sys
ROOT = Path(__file__).resolve().parents[1]
SCOPE = ROOT / "checksums/CHECKSUM-SCOPE.txt"
OUT = ROOT / "checksums/SHA256SUMS.txt"
if not SCOPE.exists():
    print("ERROR: missing checksums/CHECKSUM-SCOPE.txt")
    sys.exit(1)
rows = []
for raw in SCOPE.read_text(encoding="utf-8").splitlines():
    rel = raw.strip()
    if not rel or rel.startswith("#"):
        continue
    p = ROOT / rel
    if not p.is_file():
        print(f"ERROR: scoped file missing: {rel}")
        sys.exit(1)
    rows.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {rel}")
OUT.write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"Wrote {len(rows)} scoped checksums.")
