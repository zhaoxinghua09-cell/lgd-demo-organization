# Public Changelog (Gate-Tracked)

This changelog records changes to the public-facing objects of this repository.
Every entry follows the format: **date | change | basis**.
It is a neutral, outward-facing record; it intentionally excludes internal paths,
internal account names, and unpublished process details. Internal change records
are kept outside this public file.

## Build history

| Date | Change | Basis |
|---|---|---|
| 2026-10-16 | Repository skeleton created: directories `registry/`, `evidence/{evaluations,reverification,tools}`, `gates/`, `verify/`, with the public skill registry index (SK-001..SK-113). | `registry/skills.md` |
| 2026-10-16 | Evidence vendored into the repository: two independent evaluation reports (`verified-agent-identity` v2.1, `silent-failure-catalog` v1.1), one second-round independent reverification log, and the two reproducibility driver scripts the evaluator ran. | `evidence/` tree |
| 2026-10-16 | Public documentation completed: repository `README.md`, the `AGENTS.md` constitution, this changelog, the public badge register (`gates/badges.md`), the outsider verification guide (`verify/HOW_TO_VERIFY.md`), and the one-command verification script (`verify/run_verify.py`). | Repository root and `verify/` |
| 2026-10-16 | `README.md` bilingual completion (full Chinese section added after the full English section) and the License statement corrected to match the committed `LICENSE` file (MIT, Copyright (c) 2026 Zhao Xinghua); the earlier "no LICENSE file committed / All Rights Reserved" note was stale. | Committed `LICENSE` file; bilingual delivery requirement |
| 2026-10-16 | New public policy file `SECURITY.md` added: credential, vulnerability-reporting, dependency, and operational security rules, each mapped to the LGD three laws. One internal vault directory name removed during the pre-release leak rescan (published policy must not name local directories). | Public security policy draft; 12-category leak rescan (zero residual) |

## Gate-tracked public objects

| CHG | Object | Status |
|---|---|---|
| CHG-101 | README.md | closed |
| CHG-102 | AGENTS.md | closed |
| CHG-103 | verify/HOW_TO_VERIFY.md | closed |
| CHG-104 | verify/run_verify.py | closed |
| CHG-105 | gates/CHANGELOG.md | closed |
| CHG-106 | gates/badges.md | closed |

Status legend: `open` — under review, gate not yet passed; `closed` — gate passed and the object is frozen.

## Notes

- All archived evaluation and reverification reports are dated 2026-10-16 in their own headers; this changelog adopts that date as the build date.
- `evidence/` is treated as a frozen snapshot (see `AGENTS.md`); corrections to evidence are not recorded here as changes — they go through a discussion, never an edit.
