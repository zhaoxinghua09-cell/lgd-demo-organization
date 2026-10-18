# LGD Demo Organization — Public Verification Repository (English)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3 stdlib](https://img.shields.io/badge/Python-3%20standard%20library-blue.svg)](verify/run_verify.py)
[![Evidence: triple](https://img.shields.io/badge/evidence-triple%20evidence-2ea44f.svg)](evidence/)
[![AI-friendly](https://img.shields.io/badge/AI--friendly-llms.txt-101E2C.svg)](llms.txt)

This is the English-only mirror of the project README. The canonical, bilingual
README lives in [README.md](README.md).

A demonstration organization operated under the LGD three-law constitution. This
repository is the publicly verifiable sample: the claims it makes about its assets
can be checked by any outside reader, without trusting the operator.

## Quick Start

Verify this public sample yourself — only Python 3 (standard library):

```bash
git clone https://github.com/zhaoxinghua09-cell/lgd-demo-organization.git
cd lgd-demo-organization
python verify/run_verify.py
```

Read the printed table: every line is `PASS`, `FAIL`, or `SKIP`. Cross-check the
cited numbers against the source documents. Guide: `verify/HOW_TO_VERIFY.md`.

## The no-self-certification policy

We do not ask you to trust our word. Every external-facing claim is backed by
three independent evidence layers:

1. **Independent evaluator reports** — outsider perspective, run on a fresh copy,
   never on the asset itself (`evidence/evaluations/`, `evidence/reverification/`).
2. **Reproducible tooling** — the same scripts the evaluator ran, archived under
   `evidence/tools/`; re-run them and compare the numbers.
3. **External institutional time-stamps** — a DOI or equivalent no single party can
   backdate. Example archived claim: `silent-failure-catalog` v0.1.3, DOI
   `10.5281/zenodo.23301091`. Honest boundary: this demo repo itself has not yet
   received a DOI / SWH / arXiv deposit.

## Directory layout

| Path | Purpose |
|---|---|
| `registry/skills.md` | Public skill registry: 113 entries (SK-001..SK-113), index only. |
| `evidence/evaluations/` | Independent evaluation reports. |
| `evidence/reverification/` | Second-round reverification logs. |
| `evidence/tools/` | The reproducible scripts the evaluator ran (archived, read-only). |
| `gates/badge_program.md` | Gate/badge program definition. |
| `gates/badges.md` | Public badge issuance register. |
| `verify/HOW_TO_VERIFY.md` | Outsider verification guide. |
| `verify/run_verify.py` | One-click verification script (Python stdlib). |

## Constitution (short form)

Full text in `AGENTS.md`. In short: Registry (every asset is registered before
use), Evidence (every claim carries evidence; evidence files are read-only), and
Gates (nothing is released before it passes its gate).

## License

This repository is licensed under the **MIT License** (see the `LICENSE` file;
Copyright (c) 2026 Zhao Xinghua (Steven Zhao)). Do not reuse the
"LGD-evaluated" badge mark outside the cited reports.

## Signatories

- **Steven Zhao** — Independent Researcher
- **SynomosAI** — unregistered entity (personal demonstration; not a statement by
  any legal entity)

Contact: zhaoxinghua09@gmail.com ｜ ORCID 0009-0001-0512-1237
