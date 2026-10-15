# How to Verify This Repository (Outsider Guide)

## Steps

1. Clone this repository to a fresh directory.
2. Prepare the environment: **Python 3.9 or newer** (the verification script uses the standard library only — no pip install needed). Node.js is optional; it is used only when the script can re-run the archived `verified-agent-identity` matrix on a machine that also has that external asset checked out.
3. Read `README.md` for the policy and the directory layout.
4. Run the one-click script:

   ```
   python verify/run_verify.py
   ```

5. Read the printed table. Every line is marked `PASS`, `FAIL`, or `SKIP`.
6. Cross-check the cited numbers against the source documents:
   - Registry row count → `registry/skills.md` (expect SK-001..SK-113, 113 data rows).
   - Evaluation verdicts → `evidence/evaluations/*.md` (look for the `结论：通过` line and the `LGD-evaluated` badge block).
   - Reverification logs → `evidence/reverification/*.txt` (per-command exit codes and `判定: PASS` lines).

## Claims ↔ evidence map (all paths are relative to the repository root)

| Public claim in this repo | Evidence backing it | How to check |
|---|---|---|
| 113 skills registered (SK-001..SK-113) | `registry/skills.md` | `run_verify.py` registry-format step; or count `SK-` rows manually |
| `verified-agent-identity`: 21/21 tests PASS, LGD-2 full certification, zero S0/S1 | `evidence/evaluations/verified-agent-identity_evaluation_v2.md`; archived driver `evidence/tools/matrix_test.py` | `run_verify.py` matrix step re-runs the driver when node + the external asset checkout are present; otherwise read the archived report and its §6 reproduction commands |
| `silent-failure-catalog` toolchain: 10/10 checks PASS; 14 catalog entries; 21 gates; 38/38 defect closure; mutation score 1.000 | `evidence/evaluations/silent-failure-catalog_evaluation_v1.md`; per-command exit codes in `evidence/reverification/silent-failure-catalog_second-round_independent_reverification.txt` | `run_verify.py` evidence-integrity step; or read the reverification log's summary table |
| External time-stamp: archived DOI `10.5281/zenodo.23301091` (v0.1.3), concept DOI `10.5281/zenodo.23051637` | Cited inside both SFC evidence files (CFF 1.2.0 schema validation) | Resolve the DOI on zenodo.org |
| Badge issuances | `gates/badge_program.md`; public register `gates/badges.md` | Each row in `gates/badges.md` points to its evidence file above |

## What is reproduced with one click

| Check | Reproducible here? |
|---|---|
| Archived tool self-check (compile + minimal execution against a temp fixture) | Yes |
| Archived scanner executed against the shipped registry index | Yes (expected: 0 evaluated, 1 skipped — flat index, no per-skill SKILL.md) |
| Registry format (header row, 113 rows, sequential SK-xxx IDs) | Yes |
| Evidence files exist, are non-empty, and contain documented certification keywords | Yes |
| Archived matrix driver re-run (real PASS/FAIL counts) | Only when node and the external asset checkout are present; otherwise honestly SKIPPED |

## What is NOT reproduced with one click (honest boundary)

- **Full 113-skill AI-readiness scan.** It requires a public skill collection on disk. If you have one, run:

  ```
  python verify/run_verify.py --skills-dir /path/to/skills-collection
  ```

  The script scans every subdirectory containing a `SKILL.md` with the archived scanner, prints a PASS / FIX_REQUIRED summary, and removes the reports it generated so the input collection is left untouched. If no public skill collection is available on the machine, the full scan is skipped by design — this repository then provides the registry index and the archived scan evidence instead.
- **verified-agent-identity 21/21 matrix.** The archived driver (`evidence/tools/matrix_test.py`) requires a Node.js environment plus the evaluated asset repository with its dependencies installed. When both are present on the machine, `run_verify.py` re-runs the matrix for real and prints the reproduced PASS/FAIL counts; on any other machine the step is marked `SKIP` with the reason, and the raw 21/21 output remains archived in `evidence/evaluations/verified-agent-identity_evaluation_v2.md`.

## Exit code convention

`run_verify.py` exits `0` when no check is `FAIL`, and `1` otherwise. `SKIP` lines are recorded honestly and are never counted as `PASS`.
