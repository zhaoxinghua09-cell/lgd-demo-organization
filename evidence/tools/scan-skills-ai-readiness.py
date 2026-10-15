#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan-skills-ai-readiness.py — SKILL.md AI 可读性扫描 + 整改建议生成器
专业评测号出品（示范用例：整改工具）
用法:
  python scan-skills-ai-readiness.py <skill_dir> [skill_dir...]
输出:
  <skill_dir>/AI_READINESS_REPORT.md  — 人读版（含雷达评分表 + 整改清单）
  <skill_dir>/ai_readiness.yaml      — AI 可读版（整改建议 yaml，AI 可直接执行）
理论依据: LGD 三律（Registry 入册 / Evidence 取证 / Gates 过门）+ 静默失败目录（SKILL.md 缺协议 = 盲门）
"""
import os, sys, re, datetime

def check_frontmatter(path):
    """检查 SKILL.md frontmatter 完整性"""
    text = open(path, encoding='utf-8', errors='replace').read()
    issues = []
    if not text.startswith('---'):
        issues.append(('F1', 'frontmatter', '缺少 frontmatter 分隔符（--- 开头）', 'S1'))
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        return issues, {}, text
    fm = m.group(1)
    has_name = re.search(r'^name\s*:', fm, re.M)
    has_desc = re.search(r'^description\s*:', fm, re.M)
    if not has_name:
        issues.append(('F2', 'name', 'frontmatter 缺 name 字段', 'S1'))
    if not has_desc:
        issues.append(('F3', 'description', 'frontmatter 缺 description 字段（AI 检索关键）', 'S1'))
    desc_len = 0
    dm = re.search(r'^description\s*:\s*(.+)', fm, re.M)
    if dm:
        desc_len = len(dm.group(1).strip())
        if desc_len < 30:
            issues.append(('F4', 'description', f'description 过短（{desc_len} 字），AI 无法理解用途', 'S2'))
    return issues, {'has_name': bool(has_name), 'has_desc': bool(has_desc), 'desc_len': desc_len}, text

def check_protocol(path, text):
    """检查是否有明确调用协议（AI 自主可插拔关键）"""
    issues = []
    for kw in ['Usage', '用法', '调用', '何时用', '## 流程', 'flow']:
        if kw in text:
            return [], True
    issues.append(('P1', 'protocol', '正文缺调用协议（Usage/用法/流程），AI 不知如何调用', 'S2'))
    return issues, False

def check_llms_txt(skill_dir):
    """检查 llms.txt / AGENTS.md 是否存在（AI 发现性）"""
    found = []
    for f in ['llms.txt', 'AGENTS.md', 'README.md']:
        if os.path.exists(os.path.join(skill_dir, f)):
            found.append(f)
    issues = []
    if 'llms.txt' not in found and 'README.md' not in found:
        issues.append(('L1', 'discovery', '缺 llms.txt/README.md，AI 与人对资产理解入口缺失', 'S2'))
    return issues, found

def score(issues):
    """八属性粗略评分（0-5），用于雷达图"""
    s = {'功能性': 5, '易用性': 5, '可维护性': 5, '可移植性': 5, '安全性': 5, '可靠性': 5, '兼容性': 5, 'AI友好': 5}
    for code, _, _, lv in issues:
        drop = 1.5 if lv == 'S1' else 1.0
        if code.startswith('F'):
            s['功能性'] = max(0, s['功能性'] - drop)
            s['可维护性'] = max(0, s['可维护性'] - drop)
        if code.startswith('P'):
            s['AI友好'] = max(0, s['AI友好'] - drop)
            s['易用性'] = max(0, s['易用性'] - drop)
        if code.startswith('L'):
            s['AI友好'] = max(0, s['AI友好'] - 0.5)
            s['可移植性'] = max(0, s['可移植性'] - 0.5)
    return s

FIX_THEORY = {
    'F1': ('在文件最顶部加 `---` 起始行', 'frontmatter 是 AI 解析技能的入口，缺分隔符=盲门（静默失败目录 E1）'),
    'F2': ('补 `name: <技能名>` 字段', 'name 是 Registry 注册标识（LGD 律一：一切入册）'),
    'F3': ('补 `description: <一句话用途>`（≥30 字，含触发场景与能力）', 'description 是 AI 检索/路由的依据（AI 友好第一铁律）'),
    'F4': ('扩写 description 至 ≥30 字，说明做什么、何时用、产出什么', 'description 过短 → AI 无法判断何时调用 → 静默失败（E2 盲门）'),
    'P1': ('在正文加 `## 何时用` / `## 用法` / `## 流程` 章节，写明调用步骤与参数', '调用协议缺失 = 盲门（E2）；补协议 = Gates 可见（LGD 律三）'),
    'L1': ('新建 README.md（或 llms.txt）：一行简介 + 指向 SKILL.md', '发现性缺失 → AI 检索不到 = 幽灵资产（LGD 律一：未入册即不可见）'),
}

def main():
    targets = sys.argv[1:]
    if not targets:
        print('Usage: python scan-skills-ai-readiness.py <skill_dir> [...]'); return
    for d in targets:
        sk = os.path.join(d, 'SKILL.md')
        if not os.path.exists(sk):
            print(f'[SKIP] {d}: 无 SKILL.md'); continue
        issues, fm, text = check_frontmatter(sk)
        p_issues, has_proto = check_protocol(sk, text)
        l_issues, found = check_llms_txt(d)
        all_issues = issues + p_issues + l_issues
        scores = score(all_issues)
        date = datetime.date.today().isoformat()
        # --- 人读版 ---
        md = f"""# AI 可读性评测报告（整改版）
资产：{d}  日期：{date}  评测：专业评测号

## 质量雷达（1-5）
| 属性 | 得分 |
{chr(10).join(f'| {k} | {v:.1f} |' for k, v in scores.items())}

## 发现 {len(all_issues)} 项 / 整改清单
| ID | 级别 | 问题 | 整改动作 | 理论依据 |
{chr(10).join(f"| {c} | {lv} | {issue} | {FIX_THEORY.get(c, ('见 yaml', '见 yaml'))[0]} | {FIX_THEORY.get(c, ('', ''))[1]} |" for c, _, issue, lv in all_issues)}

## 结论
{'✅ 达标（0 项 S1+）' if not any(lv == 'S1' for _, _, _, lv in all_issues) else f'⚠️ 需整改 {sum(1 for _,_,_,lv in all_issues if lv=="S1")} 项 S1'}
"""
        open(os.path.join(d, 'AI_READINESS_REPORT.md'), 'w', encoding='utf-8').write(md)
        # --- AI 可读版 ---
        y = []
        for c, _, issue, lv in all_issues:
            fx = FIX_THEORY.get(c, ('修复 ' + issue, '见 v2 规范'))
            y.append(f"- id: {c}\n  level: {lv}\n  issue: {issue}\n  fix: \"{fx[0]}\"\n  verify: \"复跑本扫描，该条消失\"\n  theory: \"{fx[1]}\"")
        ai = f"""# AI Readiness Fix Instructions
asset: {d}
scanned: {date}
verdict: {'PASS' if not any(lv=='S1' for _,_,_,lv in all_issues) else 'FIX_REQUIRED'}
findings:
{chr(10).join(y) if y else '- none'}
"""
        open(os.path.join(d, 'ai_readiness.yaml'), 'w', encoding='utf-8').write(ai)
        print(f'[OK] {d}: {len(all_issues)} 项发现 → AI_READINESS_REPORT.md + ai_readiness.yaml')
        for c, _, issue, lv in all_issues:
            print(f'  [{lv}] {c}: {issue}')

if __name__ == '__main__':
    main()
