from pathlib import Path
import json, re, sys
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
errors = []

# 1. All JSON parses.
for p in ROOT.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"JSON parse failed: {p.relative_to(ROOT)}: {e}")

# 2. All schemas are valid Draft 2020-12 schemas.
schemas = {}
for p in (ROOT/"schemas").glob("*.schema.json"):
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(obj)
        schemas[p.name] = obj
    except Exception as e:
        errors.append(f"Schema invalid: {p.name}: {e}")

# 3. Valid fixtures validate against matching schemas.
mapping = {
    "delivery-evidence.valid.json":"delivery-evidence.schema.json",
    "governance-commitment.valid.json":"governance-commitment.schema.json",
    "change-event.valid.json":"change-event.schema.json",
    "authority-decision.valid.json":"authority-decision.schema.json",
    "milestone-evidence.valid.json":"milestone-evidence.schema.json",
    "benefit-evidence.valid.json":"benefit-evidence.schema.json",
    "risk-item.valid.json":"risk-item.schema.json",
    "contradiction-finding.valid.json":"contradiction-finding.schema.json",
    "drift-finding.valid.json":"drift-finding.schema.json",
    "ai-interpretation.valid.json":"ai-interpretation.schema.json",
    "human-decision.valid.json":"human-decision.schema.json",
    "audit-event.valid.json":"audit-event.schema.json",
    "executive-recommendation.valid.json":"executive-recommendation.schema.json",
    "final-output.valid.json":"final-output.schema.json",
}
for fn, sn in mapping.items():
    data = json.loads((ROOT/"fixtures/valid"/fn).read_text(encoding="utf-8"))
    v = Draft202012Validator(schemas[sn], format_checker=FormatChecker())
    es = list(v.iter_errors(data))
    if es:
        errors.append(f"Valid fixture failed {fn}: " + "; ".join(e.message for e in es))

# 4. Invalid fixtures must fail.
invalid_mapping = {
    "ai-interpretation.invalid.json":"ai-interpretation.schema.json",
    "final-output.invalid.json":"final-output.schema.json",
}
for fn, sn in invalid_mapping.items():
    data = json.loads((ROOT/"fixtures/invalid"/fn).read_text(encoding="utf-8"))
    v = Draft202012Validator(schemas[sn], format_checker=FormatChecker())
    if not list(v.iter_errors(data)):
        errors.append(f"Invalid fixture unexpectedly passed: {fn}")

# 5. Sample final output validates.
sample = json.loads((ROOT/"sample-outputs/delivery-covenant-decision-envelope.sample.json").read_text(encoding="utf-8"))
v = Draft202012Validator(schemas["final-output.schema.json"], format_checker=FormatChecker())
es = list(v.iter_errors(sample))
if es:
    errors.append("Sample final output invalid: " + "; ".join(e.message for e in es))

# 6. Relative Markdown links exist.
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for p in ROOT.rglob("*.md"):
    txt = p.read_text(encoding="utf-8")
    for target in link_re.findall(txt):
        if target.startswith(("http://","https://","#","mailto:")):
            continue
        clean = target.split("#",1)[0]
        if not clean:
            continue
        if not (p.parent/clean).resolve().exists():
            errors.append(f"Broken relative link in {p.relative_to(ROOT)} -> {target}")

# 7. Public landing documents cannot make selected unsupported status claims.
for rel in ["README.md","RELEASE_NOTES.md"]:
    txt=(ROOT/rel).read_text(encoding="utf-8").lower()
    # exact positive-claim patterns only; explanatory negations are allowed.
    bad_patterns=[
        r"\bwe are production ready\b",
        r"\bthis project is production ready\b",
        r"\benterprise proven\b",
        r"\bexternally certified\b",
        r"\bworld.?first\b",
        r"\bfully autonomous\b"
    ]
    for pat in bad_patterns:
        if re.search(pat, txt):
            errors.append(f"Unsupported public claim pattern in {rel}: {pat}")


# 8. GitHub Actions must be pinned to full immutable SHAs.
workflow = (ROOT/".github/workflows/ci.yml").read_text(encoding="utf-8")
for action_ref in re.findall(r"uses:\s*([^\s#]+)", workflow):
    if "@" not in action_ref:
        errors.append(f"Action missing ref: {action_ref}")
        continue
    _, ref = action_ref.rsplit("@",1)
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        errors.append(f"GitHub Action is not pinned to full SHA: {action_ref}")

# 9. Required governance/quality files exist.
required_files = [
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/dependabot.yml",
    "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md",
    "docs/EXECUTIVE-ONE-PAGER.md",
    "docs/DOCUMENTATION-QUALITY-CHECKLIST.md",
    "evidence/GATE-0-EVIDENCE-INDEX.md",
    "evidence/project-status.json",
    "evidence/release-evidence-manifest.json",
    "six-sigma/OPERATIONAL-DEFINITIONS.md",
    "six-sigma/PROCESS-EXCELLENCE-CHALLENGE-QUESTIONS.md",
    "six-sigma/DEFECT-TAXONOMY.md",
    "six-sigma/CONTROL-PLAN.md",
    "pmp/CHANGE-CONTROL-PLAN.md",
    "pmp/CONFIGURATION-MANAGEMENT-PLAN.md",
    "pmp/RISK-REGISTER.md",
    "pmp/RACI.md",
    "pmp/BENEFITS-MANAGEMENT-PLAN.md",
    "architecture/ADR-001-DETERMINISTIC-FIRST.md",
]
for rel in required_files:
    if not (ROOT/rel).exists():
        errors.append(f"Required governance file missing: {rel}")

# 10. Status manifest may not overclaim current implementation.
status = json.loads((ROOT/"evidence/project-status.json").read_text(encoding="utf-8"))
if status["claims"].get("verifiedPortfolioBuild"):
    errors.append("Verified Portfolio Build cannot be true in Gate 0 starter.")
if status["claims"].get("ciGreenOnGitHub"):
    errors.append("CI Green cannot be pre-claimed before a GitHub Actions run exists.")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Checked {len(list(ROOT.rglob('*.json')))} JSON files and {len(schemas)} Draft 2020-12 schemas.")
