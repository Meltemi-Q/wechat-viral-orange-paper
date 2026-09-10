#!/usr/bin/env python3
"""去AI味检查器：检测文章中的AI痕迹，输出评分和问题清单。
用法: python check_ai_taste.py 文章.txt
"""
import re, sys

BANNED_TITLE = [r"真正.{1,6}的人", r"成年人最", r"一个人.{1,10}(迹象|标志)", r"人到中年", r"人这一生", r"人生下半场", r"越来越.{1,6}的人"]
BANNED_BODY = ["正如", "曾经说过", "事实上", "众所周知", "不难发现", "由此可见", "生活中，我们", "在这个快节奏", "在当今社会", "随着社会的发展"]
BANNED_END = ["愿你", "共勉", "余生", "你若盛开"]
VAGUE = ["看过一个故事", "有人说", "有这样一个人", "听过一句话"]
PERSONAL = [r"我[的那]?(同事|朋友|老板|室友|妈|爸|老公|老婆)", r"(上周|昨天|那天|去年|上个月).{0,15}我", r"我(试过|哭了|愣了|合上书|盯着)"]

def check(text):
    issues, score = [], 0
    lines = text.strip().split("\n")
    title = lines[0] if lines else ""
    body = "\n".join(lines[1:])
    for p in BANNED_TITLE:
        if re.search(p, title):
            issues.append(f"[标题] 禁用句式: {p}"); score += 2
    for w in BANNED_BODY:
        n = body.count(w)
        if n: issues.append(f"[正文] 禁用词「{w}」x{n}"); score += n
    quotes = len(re.findall(r"说过|所说|曾说", body))
    if quotes > 1: issues.append(f"[正文] 名言引用{quotes}次(上限1)"); score += quotes - 1
    for w in VAGUE:
        if w in body: issues.append(f"[正文] 虚化表达「{w}」→改具体个人时刻"); score += 2
    tail = body[-100:]
    for w in BANNED_END:
        if w in tail: issues.append(f"[结尾] 禁用「{w}」"); score += 2
    if not any(re.search(p, body) for p in PERSONAL):
        issues.append("[全文] 未检测到个人时刻(具体场景/对话/自嘲)"); score += 3
    long_sents = [s for s in re.split(r"[。！？]", body) if len(s) > 40]
    if len(long_sents) > 3: issues.append(f"[风格] 超长句{len(long_sents)}处(>40字)"); score += 1
    rating = min(5, 1 + score * 0.25)
    return rating, issues

if __name__ == "__main__":
    path = sys.argv[1]
    text = open(path, encoding="utf-8", errors="ignore").read()
    # 未填的填空标记：直接拒绝，不打分
    unfilled = re.findall(r"【补一件事[^】]*】", text)
    if unfilled:
        print(f"❌ 还有 {len(unfilled)} 处没填，不能推送：")
        for u in unfilled: print(" -", u[:60] + ("…" if len(u) > 60 else ""))
        sys.exit(2)
    rating, issues = check(text)
    print(f"AI味评分: {rating:.1f}/5  ({'通过' if rating < 2.5 else '需要改稿'})")
    for i in issues: print(" -", i)
    if not issues: print(" 无明显AI痕迹")
