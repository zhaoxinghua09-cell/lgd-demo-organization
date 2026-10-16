# Security Policy

This repository is a publicly verifiable demonstration organization operated
under the LGD three-law constitution (Registry, Evidence, Gates). This policy
describes how credentials, vulnerabilities, dependencies, and release
operations are handled, and maps each rule back to the three laws.

## Scope and supported versions

- This policy applies to the latest pushed revision of this repository.
- The frozen snapshots under `evidence/` are read-only by constitution. A
  suspected defect in an archived evidence file is raised as a discussion,
  never fixed by editing the frozen file.

## 1. Credential Policy

- **Zero plaintext credentials in the repository.** No access tokens,
  passwords, API keys, or private keys are committed, in code, documentation,
  or history rewrites.
- **Local credential storage.** Machine credentials are kept in a local
  DPAPI-protected encrypted vault directory, outside the working tree. The
  vault directory is never copied into, shipped with, or archived alongside
  this repository.
- **Git credentials via helper.** Git remotes use bare URLs; authentication
  goes through the platform credential helper. `.git/config` must not embed
  credentials in remote URLs.
- **Pre-release leak scan.** Before any release, the changed files are
  scanned for internal drive-letter paths, personal mailboxes,
  account-bearing URLs, and token-shaped strings. A positive hit blocks the
  release until it is resolved.

## 2. Vulnerability Reporting

- **Where to report.** Report a suspected vulnerability through a private
  GitHub Security Advisory for the public mirror (or a private security
  issue, if advisories are not yet enabled). Do not open a public issue for
  unpatched vulnerabilities.
- **What to include.** A reproducible description is required: the affected
  path, exact steps to reproduce, expected versus observed behavior, and the
  impact judged likely. Reports without reproduction steps may be deferred.
- **Non-public disclosure.** Reporters are asked to give the maintainer a
  reasonable window to reproduce and fix before any public mention. There is
  no bug bounty; acknowledgement in the public changelog is offered at the
  reporter's request.
- **Out of scope.** Claims about the external assets archived under
  `evidence/` belong to their own upstreams; this repository only stores
  frozen evaluation reports about them.

## 3. Dependency Policy

- **No external runtime dependencies.** The verification tooling
  (`verify/run_verify.py`, `evidence/tools/`) uses the Python standard
  library only; the documented verification step installs nothing.
- **No third-party CDN assets.** The repository does not rely on content
  delivery networks (including bootcdn, staticfile, or polyfill.io) for
  functional code.
- **Dependency provenance.** Any future dependency list must record the
  source and origin of each entry; unverifiable sources are rejected.
- **Supply-chain review is a release gate.** A change that introduces a
  dependency is not released until its provenance and the absence of
  post-install network behavior are checked and the result is recorded
  under `gates/`.

## 4. Operational Security

- **Pre-release rescan.** Before pushing a release, re-run
  `python verify/run_verify.py` together with the leak scan. Both must show
  no FAIL before the gate record is closed.
- **Git configuration hygiene.** At release time, `.git/config` is checked:
  remote URLs contain no embedded credentials.
- **Sensitive local directories are not shipped.** Vault copies and local
  backups stay outside the repository tree; release packaging excludes
  hidden local state.
- **Frozen evidence stays frozen.** Because `evidence/` is immutable, every
  security conclusion in it remains independently re-checkable by an outside
  reader.

## LGD Security Mapping

| Law | Security meaning in this repository |
|---|---|
| **Registry** | Assets, credentials, and dependencies are all registered before use — an unlisted credential or dependency does not exist here. |
| **Evidence** | Security conclusions must be reproducible: the scripts and reports an evaluator ran are archived, and an outside reader can re-run them. |
| **Gates** | Leak scanning, code audit, and supply-chain review are release gates — nothing is released before it passes. |
