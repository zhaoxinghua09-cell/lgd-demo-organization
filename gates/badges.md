# Badge Issuance Register (Public)

Source of truth for the badge program: `gates/badge_program.md` (v1.0).
This register lists **only** issuances that are backed by reports vendored under
`evidence/`. No badge, certification level, or pass count is recorded here
without a cited evidence file; anything not yet evaluated is a status note,
not an issuance.

- **Issuing body:** the independent evaluation identity (outsider perspective;
  evaluations executed on freshly copied environments, never on the asset itself).
- **Program reference:** LGD-1 basic / LGD-2 full / LGD-3 expert certification
  grading, plus the LGD-evaluated text badge, as defined in `gates/badge_program.md`.

## Issued badges

| Date | Asset | Badge / certification | Documented result | Evidence (repo-relative) |
|---|---|---|---|---|
| 2026-10-16 | `verified-agent-identity` | LGD-evaluated text badge; **LGD-2 full certification** | 21/21 tests PASS; two independent rounds agree; zero S0/S1 defects; ISO/IEC 25010 eight attributes all pass; theory coverage matrix 8/8 lines PASS. | `evidence/evaluations/verified-agent-identity_evaluation_v2.md`; driver: `evidence/tools/matrix_test.py` |
| 2026-10-16 | `silent-failure-catalog` (governance toolchain) | LGD-evaluated text badge; **LGD-2 full certification** with adversarial self-justification (mutation testing) | Toolchain 10/10 checks PASS. Second-round independent reverification reproduced: 12 of 13 scripts exit code 0; the single non-zero exit code (`gate-lint` = 1) is the disclosed expected false-positive channel, not a defect. Reproduced values: 14 catalog entries, 21 gates, 38/38 defect closure, mutation score 1.000 (one disclosed equivalent mutant), 10 dimension mutants killed + 8 load-bearing negative controls. | `evidence/evaluations/silent-failure-catalog_evaluation_v1.md`; `evidence/reverification/silent-failure-catalog_second-round_independent_reverification.txt` |

## External time-stamps carried by the evidence

- `silent-failure-catalog` release v0.1.3: archived DOI `10.5281/zenodo.23301091`; concept DOI `10.5281/zenodo.23051637` (CFF 1.2.0 schema validation; cited inside the two SFC evidence files).
- This demonstration repository itself has no DOI / SWH / arXiv deposit yet; that is stated honestly here rather than implied.

## Notes

- When the badge program promo material was drafted, the `silent-failure-catalog` row was marked "formal report pending". The formal v1.1 evaluation and the second-round independent reverification have since been vendored in this repository and are the evidence base listed above.
- No other issuances are registered here. The program records the rest of the skill portfolio as pending evaluation; that is a status, not a badge.
- Validity follows the program in `gates/badge_program.md`: one-year validity, re-evaluation triggered by major asset changes.
