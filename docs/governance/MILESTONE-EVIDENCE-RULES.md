# Milestone Evidence Rules

A milestone cannot be accepted because related stories are Done.

Required checks:
- acceptance criteria satisfied;
- required deliverables present;
- dependencies resolved or formally accepted;
- open defects assessed;
- exceptions approved where applicable;
- business/project owner confirmation present;
- acceptance authority verified;
- audit evidence linked;
- benefit measurement plan confirmed where relevant.

State model:
`not_started` → `in_progress` → `delivery_complete_unverified` → `evidence_incomplete` / `exception_approval_required` → `ready_for_human_acceptance` → `accepted` / `rejected` → `reopened`.

Missing mandatory evidence cannot produce `accepted`.
