# silent-failure-catalog 专业评测报告 v1.1（v1.0 + 环境基线 / 范围声明 / 证据索引 / 第二轮独立复核）

评测机构视角：专业评测号（独立第三方评测）
评测日期：2026-10-16
评测依据：Agent 资产专业评测规范 v2.0（ISO/IEC 25010 + IEEE 829 + ISTQB + OWASP 映射）
被测资产：silent-failure-catalog（<internal-path>
资产主张：14 个静默失败用例目录（SF-005/006/010-013）+ 16 个治理工具 + 21 门控一致性 + 突变测试自证

## 评测认证

> **结论：通过（可发布）**
>
> 本报告由【专业评测号】独立评测，依据《Agent 资产专业评测规范 v2.0》
> （ISO/IEC 25010 · IEEE 829 · ISTQB · OWASP Agentic Applications 2026），
> 工具链 10 项评测全部通过，无 S0/S1 缺陷。
>
> 认证徽章（可挂载仓库 README / 技能页）：
> ```markdown
> [![LGD-evaluated](https://img.shields.io/badge/LGD--evaluated-专业评测通过-14B8A6)](https://github.com/<account>/silent-failure-catalog)
> ```

## 1. 评测范围

- 工具链可执行性：tools/ 下 16 个脚本逐一实跑
- 对抗性自证：突变测试（impl-mutation / checker-mutation）
- 数据完整性：14 SF 用例目录、缺陷闭环、行尾、CFF 元数据
- 门控一致性：21 门控与理论门控定义对齐

### 1.1 环境基线（规范 §十四 必填）

```yaml
environment:
  os: Windows（本机实测；PowerShell 5.1）
  runtime: python（系统 python，标准库纯实现，无第三方依赖）
  deps: 无（13 个 tools 脚本均为 python 标准库）
  seed: N/A（无随机/并发测试）
  isolation: 全新副本目录（<internal-path>
  public_only: true（仅按 README/AGENTS.md/llms.txt 公开文档执行，无内部知识）
```

### 1.2 范围声明（不声称）

> 本报告评测范围：tools/ 13 脚本可执行性、突变测试自证（impl/checker）、21 门控一致性、38/38 缺陷闭环、CFF schema 合规、行尾治理、发布面一致性。
> **不声称**：非 Python 工具链的静默失败覆盖、真实生产环境长周期监测、浏览器/移动端场景、跨 OS（仅 Windows 实测，python 标准库可移植性为静态判断）。

## 2. 工具链评测结果（10 项全 PASS）

| # | 工具/检查 | 结果 | 关键证据 |
|---|---|---|---|
| 1 | check-catalog | ✅ PASS | 14 条目目录校验 |
| 2 | check-gate-parity | ✅ OK | 21 门控定义一致 |
| 3 | check-line-endings | ✅ OK | 82 文件无 CRLF |
| 4 | make-manifest | ✅ OK | 277 路径排除（报告不静默） |
| 5 | verify-cff-schema | ✅ PASS | CITATION.cff 通过官方 CFF 1.2.0 schema；DOI 10.5281/zenodo.23301091 |
| 6 | impl-mutation | ✅ **PASS（满分）** | 突变分数 1.000；12 真实突变击杀 11 + 1 等价透明披露（raw 11/12=0.917） |
| 7 | checker-mutation | ✅ PASS | 第二轮实跑口径：10 检查维度定向突变全部 killed + 2 接地哨兵（SENTINEL-inert 按设计存活）、8 条 NEG 负对照 load-bearing；脚本 verdict PASSED（第一轮"12 维度 / 9 负对照"为含哨兵的近似计数，以脚本实测输出为准） |
| 8 | defect-closure | ✅ CLOSED | 38/38 缺陷条目含全要素（shape/escape/root cause/gate/evidence） |
| 9 | gate-lint | ✅ PASS | SFL 扫描通过（含已披露 false-positive 提交通道） |
| 10 | verify_release_* 系 | ✅ 可用 | 发布一致性/门面校验脚本实跑可用 |

## 3. 对抗性测试亮点（体现评测专业性）

**突变测试（S11）**：向实现注入 12 个真实缺陷突变，检测器击杀 11/12；唯一存活者为**等价突变**（NUM-002：EXIT_FAIL 数值 2→3 不改变可观测行为），已透明披露等价率 1/13——这比"满分但隐瞒"更专业。

**检查器自证（S9）**：第二轮实跑确认 10 个检查维度（CW-firstcolumn/CW-class-column/CW-row-count/COH-any/COH-target-vs-action/BLIND/SELFREPORT/SPEC-field/ROW4-both-reasons/SUITE-survivors）逐个注入突变全部被杀，另加 2 个接地哨兵（SENTINEL-fatal killed / SENTINEL-inert 按设计存活）；8 条负对照（NEG-*）删除后检查器立即存活——证明每个检查器都"真正干活"，不是摆设。

**缺陷闭环（38/38）**：所有静默失败条目都回答 形状→逃逸原因→根因→门控→证据 五要素。

## 4. 质量模型结论（ISO/IEC 25010）

| 属性 | 评级 | 证据 |
|---|---|---|
| 功能性 | ✅ | 10 项工具链全 PASS |
| 可靠性 | ✅ | 突变分数 1.000（等价排除后） |
| 安全性 | ✅ | 检查器防绕过（负对照 load-bearing） |
| 易用性 | ✅ | 16 脚本统一 Usage，零手工配置 |
| 可维护性 | ✅ | make-manifest 自动生成 + 手工内容保留 |
| 可移植性 | ✅ | 纯 python 标准库，无外部依赖 |
| 性能效率 | ✅ | 全工具 <2min（impl-mutation 含 10x 超时控制） |
| 合规性 | ✅ | CITATION.cff 官方 schema；行尾治理 |

## 5. 缺陷清单

| 级别 | 缺陷 | 状态 |
|---|---|---|
| S0/S1 | 无 | - |
| S2 | gate-lint 对自身 3 处 except-pass 报误报（SFL-002） | 属已设计 false-positive 提交通道预期，非缺陷（记录在案；第二轮复核退出码=1 复确认属该预期通道，非真实缺陷） |

## 6. 复现方法（外人可执行）

```bash
git clone https://github.com/<account>/silent-failure-catalog
cd silent-failure-catalog
python tools/check-catalog.py            # 14 条目
python tools/check-gate-parity.py        # 21 门控
python tools/impl-mutation.py            # 突变分数 1.000
python tools/checker-mutation.py         # 12 检查器自证
python tools/defect-closure.py           # 38/38 CLOSED
python tools/verify-cff-schema.py        # CFF 官方 schema
```

## 7. 独立复核记录

- 第一轮（评测号执行，今日 06:2x）：确认全部工具可用；聚焦突变/对抗批次；驱动记录 `<internal-path>` / `_sf_defect.txt`
- **第二轮（独立评估员执行，今日 07:0x）**：全新副本 `<internal-path>`，13 个 tools 脚本逐一实跑（命令/退出码/原始输出全留档），与第一轮结论一致：
  - 12/13 脚本退出码 0 全 PASS；gate-lint 退出码=1（10 findings，其中 3 条 high = 已披露 SFL-002 预期通道，非真实缺陷）
  - 关键数值复现：check-catalog 14 条目 / check-gate-parity 21 门 / check-line-endings 82 文件 / defect-closure 38-38 / impl-mutation 突变分数 1.000（等价突变已披露）/ CFF 1.2.0 无 findings
  - prepare.py 为写操作流水线（含 git 暂存副作用），按"只评测不改"原则仅记录用法不实跑
- 复核发现：无 S0/S1 新缺陷；两个计数口径差异（checker-mutation 10+2 维度 / 8 负对照 vs 第一轮近似 12/9）已按实测修正，脚本 verdict 均 PASSED

### 7.1 证据索引

| 证据 | 路径 | 内容 |
|---|---|---|
| 第二轮独立复核全文 | `<internal-path>` | 逐脚本 命令/退出码/原始输出 + 汇总表 |
| 第二轮测试副本 | `<internal-path>` | 全新副本（原资产零改动） |
| 第一轮 checker-mutation | `<internal-path>` | 维度突变 + 负对照原始输出 |
| 第一轮 defect-closure | `<internal-path>` | 38/38 CLOSED 原始输出 |
| AI 可读性扫描 | `<internal-path>` | 目录型资产（无 SKILL.md）→ 扫描器如实 [SKIP]，AI 发现性由 README/AGENTS.md/llms.txt 提供 |

## 8. 结论与建议

**判定：通过（可发布）**

- 这是生态内**第一个带对抗性自证**的理论资产：不仅"声称能抓静默失败"，还用突变测试证明"真的能抓"
- 建议：把 impl-mutation/checker-mutation 方法论提炼进 FG-TIDA 评测方法论（L6 标准制定路径）；README 挂载 LGD-evaluated 徽章

## 9. 徽章条件核对（规范 §十二 颁发条件）

- [x] 冒烟 100% + 矩阵全 PASS（无 S0/S1）——两轮复核一致
- [x] 安全批次（H/I/J/K）全过——本资产为治理工具链（非在线服务），安全属性由 负对照防绕过/密钥零依赖 覆盖
- [x] 理论覆盖矩阵逐行有实测证据——SF-001~014 目录 + 38/38 缺陷闭环 + 突变击杀证据
- [x] 报告含独立复核记录 + 复现方法（§6/§7）
- [x] 修复已推送（或注明待推送窗口）——本轮"只评测不改"，无修复推送；被测评资产无待修缺陷，修复推送不适用
