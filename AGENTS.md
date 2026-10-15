# AGENTS.md — LGD Demo Organization Constitution

This file defines the operating rules of this repository for **both internal developers and external contributors**. The workflow is identical for both groups: what an outside contributor may change is exactly what an internal developer may change.

## The Three Laws (LGD Constitution)

1. **Registry — every asset is registered.** No skill, tool, or claim enters this repository without an entry under `registry/`. An unregistered asset is treated as non-existent.
2. **Evidence — every claim carries evidence.** Any statement about quality, pass/fail, or evaluation result must point to a document under `evidence/` produced from an outsider-run environment.
3. **Gates — no release before the gate.** An asset may be presented publicly only after its gate record (see `gates/`) shows it passed. Gate-tracked changes to public objects are recorded in `gates/changelog.md`.

## No self-certification

No statement about quality, certification, or pass/fail stands on its own wording. Every external-facing claim must cite at least one evidence layer: an independent evaluator report, a reproducible tool run, or an external institutional time-stamp (DOI / SWH / arXiv). A claim without a citation is removed, not softened. If a claim cannot be reproduced, the boundary is stated honestly in the document itself.

## Change trace

Every change to a public object (`registry/`, `gates/`, `verify/`, `README.md`, `AGENTS.md`) must be logged in `gates/changelog.md` with three fields: the **date**, **what changed**, and the **basis** (the evidence or decision that justifies it). `evidence/` is frozen — never edit it; if an evidence file is wrong, open a discussion instead.

## Hard boundaries

- **This repository never modifies the evaluated assets themselves.** Evaluations are always executed on a fresh copy; the original asset directory receives zero writes.
- **`evidence/` is read-only.** Its archived documents (evaluation reports, the reverification log, and the two archived tools) are frozen snapshots. Pull requests must not modify them. If you believe an evidence file is wrong, open a discussion; do not edit it.
- **Desensitization.** Public documents must not contain internal paths, private mailboxes, or personal accounts. If you discover one in existing content, report it in a pull request comment — do not silently scrub it.

## External contributor checklist

Before proposing any change under `registry/` or `evidence/`:

1. State the change and the claim it supports.
2. Attach the evidence that justifies the change (evaluator report, tool output, or dated gate record).
3. Run `python verify/run_verify.py` and paste the output table into your pull request.
4. Confirm: no file under `evidence/` was modified, and no internal path, mailbox, or account appears in the diff.

If any item above is missing, the change is not merged.

## Signatories

- **Steven Zhao** — Independent Researcher
- **SynomosAI** — unregistered entity
