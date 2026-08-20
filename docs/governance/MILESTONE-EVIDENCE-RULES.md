# Milestone Evidence Rules

A milestone cannot move to `accepted` from delivery status alone.

Minimum evidence checks:
- milestone acceptance criteria satisfied;
- required deliverables present;
- dependencies resolved or formally accepted;
- open defects assessed;
- exceptions approved where applicable;
- business/project owner confirmation present;
- acceptance authority verified;
- audit evidence linked;
- benefit measurement plan confirmed where relevant.

State machine:
`not_started` → `in_progress` → `delivery_complete_unverified` → `evidence_incomplete` / `exception_approval_required` → `ready_for_human_acceptance` → `accepted` / `rejected` → `reopened`

Fail-closed rule: missing mandatory evidence cannot produce `accepted`.
