# LGD Demo Organization — Public Verification Repository

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3 stdlib](https://img.shields.io/badge/Python-3%20standard%20library-blue.svg)](verify/run_verify.py)
[![Evidence: triple](https://img.shields.io/badge/evidence-triple%20evidence-2ea44f.svg)](evidence/)
[![AI-friendly](https://img.shields.io/badge/AI--friendly-llms.txt-101E2C.svg)](llms.txt)
[![Bilingual](https://img.shields.io/badge/i18n-English%20%7C%20中文-brightgreen.svg)](#-中文说明)

A demonstration organization operated under the LGD three-law constitution. This repository is the publicly verifiable sample: the claims it makes about its assets can be checked by any outside reader, without trusting the operator.

## Quick Start / 快速开始

Verify this public sample yourself — only Python 3 (standard library), no install of third-party packages.

```bash
git clone https://github.com/zhaoxinghua09-cell/lgd-demo-organization.git
cd lgd-demo-organization
python verify/run_verify.py
```

Read the printed table: every line is marked `PASS`, `FAIL`, or `SKIP`. Cross-check the cited numbers against the source documents (registry row count, evaluation verdicts, reverification exit codes). The full step-by-step guide lives in [`verify/HOW_TO_VERIFY.md`](verify/HOW_TO_VERIFY.md).

快速开始：克隆本仓后运行 `python verify/run_verify.py`，即可在本机一键核验；仅使用 Python 标准库，无需安装任何第三方依赖。

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

This repository is licensed under the **MIT License** (see the `LICENSE` file; Copyright (c) 2026 Zhao Xinghua (Steven Zhao)). Do not reuse the "LGD-evaluated" badge mark outside the cited reports.

## Signatories

- **Steven Zhao** — Independent Researcher
- **SynomosAI** — unregistered entity (not a registered organization; this repository is a personal demonstration, not a statement by any legal entity)

## Demo
- demo/lgd-ai-autonomy-and-pluggability.html — interactive walkthrough of the AI-self-remediation closed loop and the pluggable skill-package mechanism; machine-readable evidence in demo/evidence.jsonld.

---

## 中文说明

本仓是依据 LGD 三律章程运行的示范组织公开核验仓：仓内关于其资产的每一条对外声明，任何外部读者都可自行核对，无需信任运营者本人。

### 不自证原则

我们不要求您仅凭我们的一面之词。仓内每一条对外声明都由三层独立证据支撑（"三重证据"）：

1. **独立评估人报告**——以局外人视角撰写、在全新复制的环境中执行、从未在资产本体上运行的评估报告（`evidence/evaluations/`、`evidence/reverification/`）。
2. **可复现工具**——评估人实际运行过的同一批脚本归档于 `evidence/tools/`。外部读者可执行 `python verify/run_verify.py`，把打印出的数字与归档报告逐项对照。
3. **外部机构时间戳**——提交到外部注册机构的声明带有 DOI 或等效时间戳，任何单一一方都无法倒签。已归档声明示例：`silent-failure-catalog` v0.1.3 带归档 DOI `10.5281/zenodo.23301091`（概念 DOI `10.5281/zenodo.23051637`），见 `evidence/evaluations/silent-failure-catalog_evaluation_v1.md`。诚实边界：本示范仓自身尚未申请 DOI / SWH / arXiv 存档；我们如实说明，而不是暗示已有。

不具备三层证据的声明，本仓不予收录。凡是仅凭本仓无法复现的内容，我们在文中如实标注边界，而不是悄悄略去。

### 目录结构

| 路径 | 用途 |
|---|---|
| `registry/skills.md` | 公开技能注册表：113 条（SK-001..SK-113）。仅作索引；单技能调用协议随各资产本体存放。 |
| `evidence/evaluations/` | 独立评估报告（局外人视角）。 |
| `evidence/reverification/` | 第二轮独立复核日志：逐条命令退出码与原始输出。 |
| `evidence/tools/` | 评估人实际运行的可复现脚本（已归档、只读）。 |
| `gates/badge_program.md` | 门禁/徽章项目定义：通过一道门禁意味着什么。 |
| `gates/changelog.md` | 本仓内受门禁追踪的公开对象的脱敏变更日志。 |
| `gates/badges.md` | 公开徽章签发登记：仅收录 `evidence/` 下有文件支撑的签发。 |
| `verify/HOW_TO_VERIFY.md` | 面向外部读者的分步核验指南。 |
| `verify/run_verify.py` | 一键核验脚本（仅用 Python 标准库）。 |

### 如何核验

1. 把本仓克隆到一个全新目录。
2. 先读本文件，再读 `verify/HOW_TO_VERIFY.md`。
3. 运行：

   ```
   python verify/run_verify.py
   ```

4. 阅读打印出的表格。每一行都标为 `PASS`、`FAIL` 或 `SKIP`。
5. 把文中引用的数字与源文档逐项核对（注册表条数、评估结论、复核退出码）。

### 复现边界（如实说明）

- **在本仓内可一键复现：** 归档工具自检（编译 + 最小执行）、注册表格式校验、证据文件完整性（存在、非空、含认证关键词）。
- **仅凭本仓无法复现：** 完整的 113 项技能 AI 就绪度扫描与 21/21 的已验证代理身份矩阵。那需要公开技能合集与 Node.js 环境。本仓只提供注册表索引与归档证据。可选用法：

  ```
  python verify/run_verify.py --skills-dir /path/to/skills-collection
  ```

### 章程（简版）

全文见 `AGENTS.md`。简言之：

- **注册表（Registry）**——每项资产在使用前必须登记。
- **证据（Evidence）**——每条声明都带证据；证据文件只读。
- **门禁（Gates）**——任何资产在通过门禁前不得发布。

### 许可证

本仓采用 **MIT 许可证**（见 `LICENSE` 文件；版权所有 (c) 2026 赵兴华（Steven Zhao））。请勿在所引报告之外使用 "LGD-evaluated" 徽章标识。

### 署名

- **Steven Zhao（赵兴华）**——独立研究者
- **SynomosAI**——未注册实体（本仓为个人示范，不代表任何法律实体的立场）

### 演示

- `demo/lgd-ai-autonomy-and-pluggability.html`——AI 自我修复闭环与可插拔技能包机制的交互式走读；机器可读证据见 `demo/evidence.jsonld`。
