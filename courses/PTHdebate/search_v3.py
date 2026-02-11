#!/usr/bin/env python3
"""
Web search using public SearXNG instances (open-source, no CAPTCHA).
"""

import json
from datetime import datetime
from urllib.parse import quote_plus

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "requests"])
    import requests


SEARXNG_INSTANCES = [
    "https://searx.be",
    "https://search.sapti.me",
    "https://searx.tiekoetter.com",
    "https://search.ononoki.org",
]


def search_searxng(query: str, max_results: int = 5) -> list:
    """Search using SearXNG public instances."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    for instance in SEARXNG_INSTANCES:
        try:
            url = f"{instance}/search"
            params = {
                "q": query,
                "format": "json",
                "categories": "general",
            }
            resp = requests.get(url, params=params, headers=headers, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            
            results = []
            for item in data.get("results", [])[:max_results]:
                results.append({
                    "title": item.get("title", ""),
                    "link": item.get("url", ""),
                    "snippet": item.get("content", ""),
                    "engine": item.get("engine", "unknown")
                })
            
            if results:
                print(f"  ✓ Found {len(results)} results via {instance}")
                return results
        except Exception as e:
            print(f"  ⚠️ {instance}: {e}")
            continue
    
    return []


def analyze_relevance(result: dict) -> str:
    """Suggest how this source could be used in debate."""
    text = (result["title"] + " " + result["snippet"]).lower()
    
    if any(w in text for w in ["policy", "政策", "law", "government", "政府", "ministry"]):
        return "政策依据：可用于论证现状或可行性"
    elif any(w in text for w in ["research", "study", "研究", "data", "survey", "journal"]):
        return "数据支持：可用于因果论证或影响评估"
    elif any(w in text for w in ["school", "student", "学校", "学生", "teacher", "教师"]):
        return "教育案例：可用于具体实例或对比分析"
    elif any(w in text for w in ["risk", "concern", "problem", "挑战", "difficulty", "criticism"]):
        return "反方材料：可用于准备反驳或预判对方论点"
    elif any(w in text for w in ["debate", "辩论", "argument", "论证", "strategy"]):
        return "辩论技巧：可参考论证结构与策略"
    else:
        return "背景资料：可用于理解议题或开场引入"


def main():
    queries = [
        "AI literacy curriculum high school education",
        "artificial intelligence education policy",
        "debate skills strategies Mandarin Chinese",
        "high school debate argumentation techniques",
    ]
    
    all_results = []
    
    print("=" * 60)
    print("普通话辩论资料检索 - SearXNG")
    print("=" * 60)
    
    for query in queries:
        print(f"\n🔍 Searching: {query}")
        results = search_searxng(query, max_results=5)
        
        for r in results:
            r["usage"] = analyze_relevance(r)
        
        all_results.append({
            "query": query,
            "results": results
        })
        
        for r in results:
            print(f"    → {r['title'][:50]}...")

    # Save JSON
    with open("search_results.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Raw results saved to search_results.json")
    
    # Generate Markdown
    md = [
        "# 普通话辩论资料检索报告",
        "",
        f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "**辩题示例**：本院主张：应在高中阶段强制设置 AI 素养必修课。",
        "",
        "---",
        ""
    ]
    
    for item in all_results:
        md.append(f"## 🔍 检索词：{item['query']}")
        md.append("")
        
        if not item["results"]:
            md.append("*暂无结果（检索服务暂不可用）*")
            md.append("")
            continue
        
        for i, r in enumerate(item["results"], 1):
            md.append(f"### {i}. [{r['title']}]({r['link']})")
            md.append("")
            md.append(f"> {r['snippet']}")
            md.append("")
            md.append(f"**辩论用途**：{r['usage']}")
            md.append(f"*来源引擎*：{r.get('engine', 'N/A')}")
            md.append("")
        
        md.append("---")
        md.append("")
    
    md.extend([
        "## 如何使用这些资料",
        "",
        "1. **点击链接** 阅读原文全文",
        "2. **提取关键数据**（数字、引用、案例）",
        "3. **填写证据卡片**（见下方模板）",
        "4. **交叉验证**（至少两个来源确认同一事实）",
        "",
        "## 资料筛选原则",
        "",
        "| 原则 | 说明 |",
        "|------|------|",
        "| 权威性 | 政府/学术 > 主流媒体 > 博客论坛 |",
        "| 时效性 | 优先近三年发布的内容 |",
        "| 相关性 | 直接涉及高中教育与AI素养 |",
        "| 平衡性 | 同时收集正反双方材料 |",
        "",
        "## 证据卡片模板",
        "",
        "```",
        "标题：",
        "来源链接：",
        "发布日期：",
        "关键结论：",
        "用于论点：",
        "可能质疑：",
        "```",
        ""
    ])
    
    with open("demo01.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("✅ Markdown report saved to demo01.md")


if __name__ == "__main__":
    main()
