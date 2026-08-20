from pathlib import Path
import hashlib, sys
ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT/"checksums/SHA256SUMS.txt"
bad=[]
for line in MAN.read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    digest, rel = line.split("  ",1)
    p=ROOT/rel
    if not p.exists():
        bad.append(f"missing {rel}")
        continue
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got != digest:
        bad.append(f"mismatch {rel}")
if bad:
    print("CHECKSUM VERIFICATION FAILED")
    for x in bad: print(" -",x)
    sys.exit(1)
print("CHECKSUM VERIFICATION PASSED")
