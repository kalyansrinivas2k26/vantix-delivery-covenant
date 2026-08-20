from pathlib import Path
import hashlib
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/"checksums/SHA256SUMS.txt"
included = []
for p in ROOT.rglob("*"):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if str(rel).startswith(".git/") or rel == Path("checksums/SHA256SUMS.txt"):
        continue
    if rel.suffix in {".pyc"} or "__pycache__" in rel.parts:
        continue
    included.append(p)
lines=[]
for p in sorted(included, key=lambda x: str(x.relative_to(ROOT))):
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    lines.append(f"{h}  {p.relative_to(ROOT).as_posix()}")
OUT.write_text("\n".join(lines)+"\n", encoding="utf-8")
print(f"Wrote {len(lines)} checksums.")
