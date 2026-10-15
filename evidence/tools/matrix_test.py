# -*- coding: utf-8 -*-
"""verified-agent-identity 压力测试驱动：外人视角多场景矩阵
场景批次：
  A. 重复性（同一环境连跑 N 次身份创建 + 验证闭环）
  B. 参数变体（challenge 类型/DID 指定/默认）
  C. KMS 加密模式（开/关）
  D. 异常路径（错误 DID、未生成 challenge、错误签名）
  E. 网络隔离（resolver 不可达时的行为）
"""
import os, sys, subprocess, json, tempfile, shutil, time, re

SCRIPTS = r"<internal-path>"
ROOT = os.path.dirname(SCRIPTS)
PY = sys.executable

def run_node(args, home, env_extra=None, timeout=90, cwd=None):
    env = dict(os.environ)
    env["USERPROFILE"] = home
    env["HOME"] = home
    if env_extra:
        env.update(env_extra)
    try:
        r = subprocess.run(["node"] + args, capture_output=True, text=True,
                           timeout=timeout, env=env, cwd=cwd or ROOT,
                           encoding="utf-8", errors="replace")
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except subprocess.TimeoutExpired:
        return -99, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)[:200]

def new_home(base, tag):
    h = os.path.join(base, tag)
    shutil.rmtree(h, ignore_errors=True)
    os.makedirs(os.path.join(h, ".openclaw"), exist_ok=True)
    return h

results = []

def record(scene, sub, ok, detail):
    results.append((scene, sub, "PASS" if ok else "FAIL", detail[:120]))

# ============ 批次 A: 重复性（连跑 3 轮全新环境） ============
base = r"<internal-path>"
os.makedirs(base, exist_ok=True)
for i in range(1, 4):
    home = new_home(base, f"repeat_{i}")
    rc, out, err = run_node(["scripts/createNewEthereumIdentity.js"], home, cwd=ROOT)
    did = out.strip().splitlines()[-1] if out else ""
    ok = (rc == 0 and did.startswith("did:iden3:"))
    record("A-重复性", f"第{i}轮身份创建", ok, did)
    if ok:
        # 完整闭环（challenge→sign→verify）
        rc, out, err = run_node(["scripts/generateChallenge.js", "--did", did], home)
        cid = out.strip().splitlines()[-1] if out else ""
        ok2 = (rc == 0 and cid)
        record("A-重复性", f"第{i}轮challenge", ok2, cid)
        rc, out, err = run_node(["scripts/signChallenge.js", "--challenge", cid], home)
        m = re.search(r'"token"\s*:\s*"([^"]+)"', out)
        ok3 = (rc == 0 and m)
        record("A-重复性", f"第{i}轮签名", ok3, "JWT" if m else out[:80])
        if m:
            rc, out, err = run_node(["scripts/verifySignature.js", "--did", did, "--signature", m.group(1)], home)
            ok4 = ("verified" in out.lower())
            record("A-重复性", f"第{i}轮验证", ok4, out[:60])

# ============ 批次 B: 参数变体（同一身份多 challenge 类型） ============
home = new_home(base, "param")
run_node(["scripts/createNewEthereumIdentity.js"], home, cwd=ROOT)
rc, out, err = run_node(["scripts/getIdentities.js"], home)
did = ""
try:
    ids = json.loads(out)
    did = ids[0]["did"] if ids else ""
except Exception:
    pass
# B1: 数字型 challenge
rc, out, err = run_node(["scripts/generateChallenge.js", "--did", did], home)
cid1 = out.strip().splitlines()[-1] if out else ""
rc, out, err = run_node(["scripts/signChallenge.js", "--challenge", cid1], home)
m = re.search(r'"token"\s*:\s*"([^"]+)"', out)
if m:
    rc, out, err = run_node(["scripts/verifySignature.js", "--did", did, "--signature", m.group(1)], home)
    record("B-参数", "数字型challenge闭环", "verified" in out.lower(), out[:60])
# B2: 字符串型 challenge（数字加引号）
rc, out, err = run_node(["scripts/generateChallenge.js", "--did", did], home)
cid2 = out.strip().splitlines()[-1] if out else ""
rc, out, err = run_node(["scripts/signChallenge.js", "--challenge", '"%s"' % cid2], home)
m = re.search(r'"token"\s*:\s*"([^"]+)"', out)
if m:
    rc, out, err = run_node(["scripts/verifySignature.js", "--did", did, "--signature", m.group(1)], home)
    record("B-参数", "字符串型challenge闭环", "verified" in out.lower(), out[:60])
# B3: 错误 DID 验证（不存在 DID 应清晰报错）
rc, out, err = run_node(["scripts/verifySignature.js", "--did", "did:iden3:billions:main:0xDEAD", "--signature", "bad"], home)
record("B-参数", "不存在DID验证(应报错)", rc != 0, out[:60] or err[:60])

# ============ 批次 C: KMS 加密模式 ============
home = new_home(base, "kms")
rc, out, err = run_node(["scripts/createNewEthereumIdentity.js"], home,
                        env_extra={"BILLIONS_NETWORK_MASTER_KMS_KEY": "test-master-key-123"})
did = out.strip().splitlines()[-1] if out else ""
ok = (rc == 0 and did.startswith("did:"))
record("C-KMS加密", "加密模式身份创建", ok, did)
# 检查 kms.json 是否加密存储
kp = os.path.join(home, ".openclaw", "billions", "kms.json")
enc = False
if os.path.exists(kp):
    try:
        data = json.load(open(kp, encoding="utf-8"))
        if isinstance(data, list) and data and data[0].get("provider") == "encrypted":
            enc = True
    except Exception:
        pass
record("C-KMS加密", "私钥加密落盘", enc, "provider=encrypted" if enc else "plain")

# ============ 批次 D: 异常路径 ============
home = new_home(base, "abnormal")
run_node(["scripts/createNewEthereumIdentity.js"], home, cwd=ROOT)
# D1: 未生成 challenge 就 verify（应报 No challenge found）
rc, out, err = run_node(["scripts/verifySignature.js", "--did", did, "--signature", "x"], home)
record("D-异常", "未生成challenge验证(应报错)", "No challenge" in (out+err), (out+err)[:80])
# D2: 无默认 DID 环境验证（空 HOME）
home2 = new_home(base, "abnormal2")
rc, out, err = run_node(["scripts/verifySignature.js", "--did", "did:iden3:billions:main:x", "--signature", "y"], home2)
record("D-异常", "空环境验证(应报错)", rc != 0, (out+err)[:80])
# D3: signChallenge 缺参数（应报 --challenge required）
rc, out, err = run_node(["scripts/signChallenge.js"], home)
record("D-异常", "签名缺参数(应报错)", "--challenge" in err, err[:80])

# ============ 批次 E: 网络隔离（resolver 不可达） ============
home = new_home(base, "offline")
run_node(["scripts/createNewEthereumIdentity.js"], home, cwd=ROOT)
did = ""
rc, out, err = run_node(["scripts/getIdentities.js"], home)
try:
    ids = json.loads(out); did = ids[0]["did"] if ids else ""
except Exception: pass
# 用无效 proxy 环境模拟断网（node fetch 走系统代理设置）
rc, out, err = run_node(["scripts/generateChallenge.js", "--did", did], home,
                        env_extra={"HTTPS_PROXY": "http://127.0.0.1:9", "HTTP_PROXY": "http://127.0.0.1:9"})
cid = out.strip().splitlines()[-1] if out else ""
rc, out, err = run_node(["scripts/signChallenge.js", "--challenge", cid], home,
                        env_extra={"HTTPS_PROXY": "http://127.0.0.1:9", "HTTP_PROXY": "http://127.0.0.1:9"})
m = re.search(r'"token"\s*:\s*"([^"]+)"', out)
if m:
    rc, out, err = run_node(["scripts/verifySignature.js", "--did", did, "--signature", m.group(1)], home,
                            env_extra={"HTTPS_PROXY": "http://127.0.0.1:9", "HTTP_PROXY": "http://127.0.0.1:9"})
    # 断网下 verify 需远程 resolver：可能失败（预期内）——记录行为而非判定
    detail = (out[:60] or err[:80] or "verified(本地缓存)")
    record("E-网络隔离", "断网verify行为", True, detail)

# ============ 输出矩阵 ============
print("=" * 78)
print("verified-agent-identity 多场景压力测试矩阵（外人视角）")
print("=" * 78)
print("%-12s %-28s %-6s | %s" % ("场景", "子项", "结果", "细节"))
print("-" * 78)
for scene, sub, ok, detail in results:
    print("%-12s %-28s %-6s | %s" % (scene, sub, ok, detail))
fails = [r for r in results if r[2] == "FAIL"]
print("-" * 78)
print("合计: %d 项 | PASS: %d | FAIL: %d | 预期失败(异常路径): %d" % (
    len(results), len(results) - len(fails), len(fails),
    len([r for r in results if r[2] == "FAIL"])))
