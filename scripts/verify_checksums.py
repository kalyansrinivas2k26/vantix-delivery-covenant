from pathlib import Path
import hashlib, sys
ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / "checksums/SHA256SUMS.txt"
SCOPE = ROOT / "checksums/CHECKSUM-SCOPE.txt"
bad = []
if not MAN.exists():
    bad.append("missing checksums/SHA256SUMS.txt")
if not SCOPE.exists():
    bad.append("missing checksums/CHECKSUM-SCOPE.txt")
if bad:
    print("CHECKSUM VERIFICATION FAILED")
    for x in bad: print(" -", x)
    sys.exit(1)
scope = [x.strip() for x in SCOPE.read_text(encoding="utf-8").splitlines() if x.strip() and not x.strip().startswith("#")]
manifest = {}
for line in MAN.read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    parts = line.split("  ", 1)
    if len(parts) != 2:
        bad.append(f"malformed manifest line: {line}")
        continue
    manifest[parts[1]] = parts[0]
for rel in sorted(set(scope) - set(manifest)):
    bad.append(f"manifest missing scoped entry {rel}")
for rel in sorted(set(manifest) - set(scope)):
    bad.append(f"manifest has out-of-scope entry {rel}")
for rel in scope:
    p = ROOT / rel
    if not p.exists():
        bad.append(f"missing {rel}")
        continue
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if manifest.get(rel) != got:
        bad.append(f"mismatch {rel}")
if bad:
    print("CHECKSUM VERIFICATION FAILED")
    for x in bad: print(" -", x)
    sys.exit(1)
print(f"CHECKSUM VERIFICATION PASSED ({len(scope)} scoped files)")
