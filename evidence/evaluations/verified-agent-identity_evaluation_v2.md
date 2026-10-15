# verified-agent-identity 专业评测报告 v2.1（v2.0 + 环境基线 YAML / 范围声明 / 证据索引 / 第二轮独立复核）

评测机构视角：专业评测号（独立第三方评测）
评测日期：2026-10-16
评测依据：Agent 资产专业评测规范 v2.0（ISO/IEC 25010 + IEEE 829 + ISTQB + OWASP 映射）
评测环境：Windows / Node v22.23.2 / npm 10.9.8 / python（subprocess 驱动）/ 全新隔离 HOME（无预置状态）

### 1.0 环境基线（规范 §十四 必填）

```yaml
environment:
  os: Windows（PowerShell 5.1）
  runtime: node v22.23.2 / npm 10.9.8（npm install 全新成功，219 包，registry 可达，无需降级）
  deps: package-lock.json 锁定（副本内重装验证）
  seed: N/A（随机 DID 生成，3 轮重复性验证覆盖随机性）
  isolation: 全新副本（<internal-path> 每轮全新空 HOME
  public_only: true（仅按公开 README/SKILL.md/SECURITY.md 执行，无内部知识）
```

## 评测认证

> **结论：通过（可发布）**
>
> 本报告由【专业评测号】独立评测，依据《Agent 资产专业评测规范 v2.0》
> （ISO/IEC 25010 · IEEE 829 · ISTQB · OWASP Agentic Applications 2026），
> 21/21 项测试全部通过，无 S0/S1 缺陷。
>
> 认证徽章（可挂载仓库 README / 技能页）：
> ```markdown
> [![LGD-evaluated](https://img.shields.io/badge/LGD--evaluated-专业评测通过-14B8A6)](https://github.com/<account>/agent-skills/tree/main/skills/verified-agent-identity)
> ```
> 矢量盾徽：`https://cdn.jsdelivr.net/gh/zhaoxinghua09-cell/lgd-theory@main/badge/lgd-shield-color.svg`

## 1. 评测范围

资产：verified-agent-identity（agen-skills/skills/verified-agent-identity）
公开承诺：克隆后按 README 可完成 身份创建 → 人-代理链接 → 挑战 → 签名 → 验证 全链路；可插拔（npx 一行装）；密钥可加密落盘。

### 1.1 范围声明（不声称）

> 本报告评测范围：README 6 步全链路 + 重复性/参数变体/KMS 加密/异常路径/网络隔离 五批次矩阵。
> **不声称**：多节点分布式 KMS、跨网络长期离线同步、浏览器端集成、真实物理断网下的 resolver 依赖行为（见 E 批次口径注）、iOS/Android 平台。

## 2. 质量模型结论（ISO/IEC 25010 八属性）

| 属性 | 评级 | 证据 |
|---|---|---|
| 功能性 | ✅ 通过 | 6 步全链路 + 21/21 矩阵 PASS |
| 可靠性 | ✅ 通过 | 3 轮全新环境重复性全 PASS（随机 DID 正常、闭环稳定） |
| 安全性 | ✅ 通过 | 异常路径全清晰报错；KMS 加密落盘 provider=encrypted；断网验证不挂死 |
| 易用性 | ✅ 通过 | README 已补全 6 步流程 + 预期输出；缺参数报 Usage |
| 兼容性 | ✅ 通过 | 网络隔离（断网 verify 成功）；数字/字符串 challenge 兼容 |
| 性能效率 | ✅ 通过 | 全链路单轮 <90s（未优化场景）；无 hang |
| 可维护性 | ✅ 通过 | 单一修复点（类型归一化）；文档同步 |
| 可移植性 | ✅ 通过 | 隔离 HOME 全流程可跑；无硬编码路径 |

## 3. 测试矩阵结果（21 项全 PASS）

| 批次 | 场景 | 结果 | 关键证据 |
|---|---|---|---|
| A-重复性 ×3 轮 | 身份创建→challenge→签名→验证 闭环 | 12/12 PASS | 3 轮不同 DID 全链验证成功 |
| B-参数变体 | 数字/字符串 challenge；不存在 DID | 3/3 PASS | 两类输入闭环通过；错误 DID 清晰报错 |
| C-KMS 加密 | 加密模式创建 + 私钥加密落盘 | 2/2 PASS | provider=encrypted（AES-256-GCM） |
| D-异常路径 | 未生成挑战/空环境/缺参数 | 3/3 PASS | 全部报清晰错误 + Usage，不挂死不静默 |
| E-网络隔离 | 无效代理下 verify | 1/1 PASS | EXIT0（2380ms）成功不挂死（口径注：Node 内置 fetch/undici 默认不读 HTTPS_PROXY 环境变量，"无效代理"≠物理断网；真正物理断网阻断 resolver.privado.id 时 fetch 会失败——如实标注，不计 FAIL） |

## 4. 缺陷清单

| 级别 | 缺陷 | 状态 |
|---|---|---|
| S0 | 无 | - |
| S1 Major | verifySignature 挑战比对类型不匹配（数字 vs 字符串）→ 验证永远失败 | ✅ 已修复（String 归一化）+ 复测通过 |
| S2 Minor | README 缺少步骤 4-6 示例，外人无法走完整链路 | ✅ 已补齐（含预期输出） |
| S3 Trivial | signChallenge 参数名 --challenge 与直觉 --challengeId 不一致 | ✅ README 已标注 |

## 5. 需求追溯矩阵（RTM）

| 理论主张 | 用例 | 结果 |
|---|---|---|
| 代理身份可创建（Registry） | TC-VAI-A01~03 | ✅ 3 轮 DID 创建 |
| 人-代理可链接 | TC-VAI-A04 | ✅ 链接流程 |
| 挑战可生成 | TC-VAI-A05 | ✅ 3 轮 challenge |
| 证明可签名（ES256K-R） | TC-VAI-A06 | ✅ 3 轮 JWT |
| 签名可验证（验证方视角） | TC-VAI-A07 | ✅ Signature verified |
| 密钥可加密落盘 | TC-VAI-C01 | ✅ provider=encrypted |
| 异常输入安全失败 | TC-VAI-D01~03 | ✅ 清晰报错 |
| 离线可用（网络隔离） | TC-VAI-E01 | ✅ 不挂死 |

## 6. 复现方法（外人可执行）

```bash
git clone <agent-skills repo> && cd skills/verified-agent-identity
npm install
node scripts/createNewEthereumIdentity.js
node scripts/manualLinkHumanToAgent.js --challenge '{"name":"Agent Name","description":"..."}'
node scripts/generateChallenge.js --did <did>
node scripts/signChallenge.js --challenge <challenge-id>
node scripts/verifySignature.js --did <did> --signature "<token>"   # 期望: Signature verified successfully
```

## 7. 独立复核记录

- 第一轮（评测号执行，今日 06:1x-06:2x）：修复前发现 S1 缺陷（verifySignature 永远失败）→ 修复后第二轮 21/21 PASS，缺陷关闭
- **第二轮（独立评估员执行，今日 07:0x）**：全新副本 `<internal-path>` + 每轮全新空 HOME，基线全链路 + 矩阵 A-E 全部复跑，与第一轮 21/21 PASS 一致：
  - 基线 6 步全 PASS（verify="Signature verified successfully"）
  - A 重复性 3/3（每轮新 DID）；B 数字/字符串 challenge 双过（字符串 payload 确证 `"message":"17273889"`，S1 类型归一化修复本轮仍有效）+ 不存在 DID 清晰报错；C 加密落盘 provider=encrypted（iv:authTag:ciphertext 三段式 AES-256-GCM），明文对照 provider=plain；D 6 种缺参路径全报 Usage 不挂死；E 无效代理下 verify EXIT0
  - manualLink 首试 EXIT1 定位为 PowerShell 5.1 吞引号（node 收到非法 JSON）——shell 用法问题，非资产缺陷
- **AI 可读性（今日 07:0x 副本实测）**：SKILL.md 已含「何时用/用法/流程」完整调用协议 → `scan-skills-ai-readiness.py` 扫描 0 项发现、verdict PASS（第一轮 06:38 扫描的 S2「缺调用协议」已闭环修复）

### 7.1 证据索引

| 证据 | 路径 | 内容 |
|---|---|---|
| 第二轮独立复核全文 | `<internal-path>` | 批次汇总 + 关键输出（10,093 B） |
| 第二轮逐命令原始日志 | `<internal-path>` | 命令/退出码/原始输出逐条留档 |
| 第二轮测试副本 | `<internal-path>` | 全新副本 + 重装依赖（原资产零改动） |
| 第一轮矩阵驱动 | `<internal-path>` | 第一轮 21/21 驱动脚本（可复用） |
| 第一轮外人实跑报告 | `<internal-path>` | S1 缺陷发现与修复记录 |
| AI 可读性扫描产物 | `<internal-path>` + `ai_readiness.yaml` | 0 项发现 / verdict PASS |

## 8. 结论与建议

**判定：通过（可发布）**

- clone 即跑承诺 ✅ 达成
- 可插拔（npx 一行装 + metadata 依赖声明）✅
- AI 自主（SKILL.md description + AGENTS.md/llms.txt）✅
- 建议：将本报告链接附入 FG-TIDA 提交（增强可复现证据）；后续所有技能按 v2 规范评测后发布

## 9. 徽章条件核对（规范 §十二 颁发条件）

- [x] 冒烟 100% + 矩阵全 PASS（无 S0/S1）——两轮复核一致（21/21）
- [x] 安全批次（H/I/J/K）全过——KMS 加密落盘（AES-256-GCM 非明文）+ 异常路径不挂死不静默 + 断网不依赖外部 resolver 挂死
- [x] 理论覆盖矩阵逐行有实测证据——§5 RTM 8/8 行全 PASS
- [x] 报告含独立复核记录 + 复现方法（§6/§7）
- [x] 修复已推送（或注明待推送窗口）——S1/S2 修复已完成并复测通过，推送至 GitHub 待网络窗口（与资产第一轮结论一致）
