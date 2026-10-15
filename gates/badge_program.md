# LGD 评测认证徽章包（推广物料）

版本：v1.0（2026-10-16）
颁发主体：专业评测号（独立评测身份）
适用：所有通过《Agent 资产专业评测规范 v2.0》评测的资产（技能/工具链/MCP/Agent）

## 一、徽章体系

| 徽章 | 样式 | 用途 |
|---|---|---|
| 文字条（shields.io） | `LGD-evaluated 专业评测通过`（品牌色 14B8A6） | README/仓库/技能页，最通用 |
| 矢量盾徽（lgd-shield） | lgd-shield-color.svg | 品牌形象展示、宣传物料 |
| 组合 | 盾徽 + 文字条 | 报告首页/官网 |

## 二、嵌入代码

### 1. GitHub README
```markdown
[![LGD-evaluated](https://img.shields.io/badge/LGD--evaluated-%E4%B8%93%E4%B8%9A%E8%AF%84%E6%B5%8B%E9%80%9A%E8%BF%87-14B8A6)](<评测报告URL>)
```

### 2. 矢量盾徽
```markdown
[![LGD-evaluated](https://cdn.jsdelivr.net/gh/zhaoxinghua09-cell/lgd-theory@main/badge/lgd-shield-color.svg)](<评测报告URL>)
```

### 3. HTML（技能市场页/官网）
```html
<a href="<评测报告URL>" target="_blank" rel="noopener" title="LGD-evaluated：专业评测通过（ISO/IEC 25010）">
  <img src="https://img.shields.io/badge/LGD--evaluated-专业评测通过-14B8A6" alt="LGD-evaluated">
</a>
```

### 4. 报告首页认证块（Markdown）
```markdown
## 评测认证
> **结论：通过（可发布）**
> 本报告由【专业评测号】独立评测，依据《Agent 资产专业评测规范 v2.0》
> （ISO/IEC 25010 · IEEE 829 · ISTQB · OWASP Agentic Applications 2026），
> <N>/<N> 项测试全部通过，无 S0/S1 缺陷。
```

## 三、颁发流程

1. 资产按 v2 规范评测（冒烟 + 矩阵 A-K + 理论覆盖矩阵 + 安全批次）
2. 门禁判定：通过（无 S0/S1，八属性达标）
3. 评测号出具正式报告（IEEE 829 模板 + 认证块）
4. 报告落 `<internal-path>`，修复推送仓库
5. 资产 README 挂载徽章（链接到报告 URL）→ 全生态推广

## 三-b、分级认证（对标 TÜV L1/L2）与再认证（对标 TÜV SÜD/SGS）

### 认证分级
| 等级 | 内容 | 徽章 |
|---|---|---|
| **LGD-1 基础认证** | 功能+易用+异常路径（矩阵 A-D/F） | 文字条 |
| **LGD-2 全面认证** | L1 + 八属性全维 + 安全批次 + 突变自证 | 文字条+盾徽 |
| **LGD-3 专家认证** | L2 + 独立双 agent 互评 + 年度监督 | 盾徽+认证编号 |

当前已签发：VAI/SFC 均为 **LGD-2 全面认证**（含对抗自证）。

### 年度再认证（对标 TÜV SÜD 年度复测）
- 徽章有效期 1 年；到期前 30 天自动触发复评（台账预警）
- 资产重大变更（版本/功能/依赖）→ 立即复评
- 再认证通过 → 徽章顺延 1 年（台账更新）

### 监督审核（对标 SGS 后续监督）
- 台账每月核对资产状态（版本/证据/徽章有效性）
- 撤销条件触发（新 S0/S1、伪造证据、门禁复评不过）→ 公告 + 台账更新
- 对外认证（B 轨）同规则：年度监督 + 变更即评

## 四、推广价值（体现专业性）

- **第三方评测身份**：评测号独立执行，外人视角，可信度高
- **标准背书**：ISO/IEC 25010 · IEEE 829 · ISTQB · OWASP——国际标准语言
- **可复现证据**：矩阵 + 复现命令 + 独立复核，经得起挑战
- **生态联动**：评测通过 → 徽章 → 挂载技能/仓库/官网 → 统一品牌（LGD-evaluated）
- **差异化**：生态内每个资产带"评测认证"，形成质量信任网

## 五、首批认证资产

| 资产 | 评测结果 | 徽章状态 |
|---|---|---|
| verified-agent-identity | 21/21 PASS（v2 报告已出） | ✅ 可挂载 |
| silent-failure-catalog 工具链 | check-catalog/check-gate-parity PASS | ⏳ 待出正式报告 |
| agent-skills 其余 130+ 技能 | 待评测 | 待评测 |
