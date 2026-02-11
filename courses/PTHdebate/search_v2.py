#!/usr/bin/env python3
"""
Alternative web search script using requests + DuckDuckGo HTML.
Falls back to scraping if API fails.
"""

import json
import re
from datetime import datetime
from urllib.parse import quote_plus

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "requests"])
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup


def search_ddg_html(query: str, max_results: int = 5) -> list:
    """Search DuckDuckGo via HTML scraping."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
    
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        
        results = []
        for item in soup.select(".result")[:max_results]:
            title_el = item.select_one(".result__title a")
            snippet_el = item.select_one(".result__snippet")
            
            if title_el:
                # Extract actual URL from DuckDuckGo redirect
                href = title_el.get("href", "")
                # DDG uses uddg parameter for actual URL
                match = re.search(r"uddg=([^&]+)", href)
                if match:
                    from urllib.parse import unquote
                    actual_url = unquote(match.group(1))
                else:
                    actual_url = href
                
                results.append({
                    "title": title_el.get_text(strip=True),
                    "link": actual_url,
                    "snippet": snippet_el.get_text(strip=True) if snippet_el else ""
                })
        return results
    except Exception as e:
        print(f"  ⚠️ Search error: {e}")
        return []


def analyze_relevance(result: dict, topic: str) -> str:
    """Suggest how this source could be used in debate."""
    title = result["title"].lower()
    snippet = result["snippet"].lower()
    
    if any(w in title + snippet for w in ["policy", "政策", "law", "法律", "government", "政府"]):
        return "政策依据：可用于论证现状或可行性"
    elif any(w in title + snippet for w in ["research", "study", "研究", "数据", "data", "survey"]):
        return "数据支持：可用于因果论证或影响评估"
    elif any(w in title + snippet for w in ["school", "student", "学校", "学生", "教育"]):
        return "教育案例：可用于具体实例或对比分析"
    elif any(w in title + snippet for w in ["risk", "concern", "问题", "挑战", "difficulty"]):
        return "反方材料：可用于准备反驳或预判对方论点"
    else:
        return "背景资料：可用于理解议题或开场引入"


def main():
    queries = [
        "AI literacy curriculum high school",
        "artificial intelligence education policy secondary school",
        "debate skills Putonghua Chinese",
        "辩论技巧 经验 中学",
    ]
    
    all_results = []
    
    print("=" * 60)
    print("普通话辩论资料检索 - HTML Scraping Method")
    print("=" * 60)
    
    for query in queries:
        print(f"\n🔍 Searching: {query}")
        results = search_ddg_html(query, max_results=5)
        
        # Add relevance analysis
        for r in results:
            r["usage"] = analyze_relevance(r, query)
        
        all_results.append({
            "query": query,
            "results": results
        })
        
        for r in results:
            print(f"  ✓ {r['title'][:50]}...")

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
            md.append("*暂无结果*")
            md.append("")
            continue
        
        for i, r in enumerate(item["results"], 1):
            md.append(f"### {i}. [{r['title']}]({r['link']})")
            md.append("")
            md.append(f"> {r['snippet']}")
            md.append("")
            md.append(f"**辩论用途**：{r['usage']}")
            md.append("")
        
        md.append("---")
        md.append("")
    
    md.extend([
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
