# Contributing / 贡献指南

Thanks for your interest in this publicly verifiable demonstration organization.
The workflow is identical for internal developers and outside contributors: what
an outside contributor may change is exactly what an internal developer may change.

## Before you change anything under `registry/` or `evidence/`

1. State the change and the claim it supports.
2. Attach the evidence that justifies the change (evaluator report, tool output,
   or dated gate record).
3. Run `python verify/run_verify.py` and paste the output table into your pull
   request.
4. Confirm: no file under `evidence/` was modified, and no internal path, mailbox,
   or account appears in the diff.

If any item above is missing, the change is not merged.

## Hard boundaries

- **`evidence/` is read-only.** Its archived documents are frozen snapshots. If you
  believe an evidence file is wrong, open a discussion; do not edit it.
- **Never modify the evaluated assets themselves.** Evaluations always run on a
  fresh copy.
- **Desensitization.** Public documents must not contain internal paths, private
  mailboxes, or personal accounts. If you discover one, report it — do not
  silently scrub it.

## Change trace

Every change to a public object (`registry/`, `gates/`, `verify/`, `README.md`,
`AGENTS.md`) must be logged in `gates/changelog.md` with three fields: the date,
what changed, and the basis (the evidence or decision that justifies it).

## Quick start for contributors

```bash
git clone https://github.com/zhaoxinghua09-cell/lgd-demo-organization.git
cd lgd-demo-organization
python verify/run_verify.py
```

Questions: zhaoxinghua09@gmail.com
