# LGD Demo Organization — Public Verification Repository

A demonstration organization operated under the LGD three-law constitution. This repository is the publicly verifiable sample: the claims it makes about its assets can be checked by any outside reader, without trusting the operator.

## The no-self-certification policy

We do not ask you to trust our word. Every external-facing claim in this repository is backed by three independent evidence layers ("triple evidence"):

1. **Independent evaluator reports** — evaluation reports written from an outsider's perspective, executed on a freshly copied environment, never on the asset itself (`evidence/evaluations/`, `evidence/reverification/`).
2. **Reproducible tooling** — the same scripts the evaluator ran are archived under `evidence/tools/`. An outside reader can execute them with `python verify/run_verify.py` and compare the printed numbers against the archived reports.
3. **External institutional time-stamps** — claims deposited with an external registry carry a DOI or equivalent time-stamp that no single party can backdate. Example archived claim: the `silent-failure-catalog` release v0.1.3 carries archived DOI `10.5281/zenodo.23301091` (concept DOI `10.5281/zenodo.23051637`), cited in `evidence/evaluations/silent-failure-catalog_evaluation_v1.md`. Honest boundary: this demonstration repository itself has not yet received a DOI / SWH / arXiv deposit; we say so rather than imply one.

A claim without all three layers is not made here. Where a claim cannot be reproduced in this repository alone, the boundary is stated honestly instead of being silently dropped.

## Directory layout

| Path | Purpose |
|---|---|
| `registry/skills.md` | Public skill registry: 113 entries (SK-001..SK-113). It is an index only; per-skill call protocols live with each asset. |
| `evidence/evaluations/` | Independent evaluation reports (outsider perspective). |
| `evidence/reverification/` | Second-round independent reverification logs: per-command exit codes and raw outputs. |
| `evidence/tools/` | The reproducible scripts the evaluator ran (archived, read-only). |
| `gates/badge_program.md` | Gate/badge program definition: what passing a gate means. |
| `gates/changelog.md` | Desensitized change log of the gate-tracked public objects in this repository. |
| `gates/badges.md` | Public badge issuance register: only issuances backed by files under `evidence/`. |
| `verify/HOW_TO_VERIFY.md` | Step-by-step outsider verification guide. |
| `verify/run_verify.py` | One-click verification script (Python standard library only). |

## How to verify

1. Clone this repository to a fresh directory.
2. Read this file, then read `verify/HOW_TO_VERIFY.md`.
3. Run:

   ```
   python verify/run_verify.py
   ```

4. Read the printed table. Every line is marked `PASS`, `FAIL`, or `SKIP`.
5. Cross-check the cited numbers against the source documents (registry row count, evaluation verdicts, reverification exit codes).

### Reproduction boundary (stated honestly)

- **Reproducible with one click inside this repository:** archived tool self-checks (compile + minimal execution), registry format validation, evidence-file integrity (existence, non-empty, certification keywords).
- **Not reproducible from this repository alone:** the full 113-skill AI-readiness scan and the 21/21 verified-agent-identity matrix. Those require the public skill collection and a Node.js environment. This repository provides the registry index and the archived evidence instead. Optional usage:

  ```
  python verify/run_verify.py --skills-dir /path/to/skills-collection
  ```

## Constitution (short form)

Full text in `AGENTS.md`. In short:

- **Registry** — every asset is registered before use.
- **Evidence** — every claim carries evidence; evidence files are read-only.
- **Gates** — nothing is released before it passes its gate.

## License

**Status: TBD.** The intended license for this repository's documentation and reproducibility scripts is CC BY 4.0. No `LICENSE` file has been committed yet; until one is added, treat all content as All Rights Reserved. Do not reuse the "LGD-evaluated" badge mark outside the cited reports.

## Signatories

- **Steven Zhao** — Independent Researcher
- **SynomosAI** — unregistered entity (not a registered organization; this repository is a personal demonstration, not a statement by any legal entity)
