#!/usr/bin/env python3
"""
Web search script for debate research using DuckDuckGo.
No API key required - uses the duckduckgo-search library.
"""

import json
from datetime import datetime

try:
    from duckduckgo_search import DDGS
except ImportError:
    print("Installing duckduckgo-search...")
    import subprocess
    subprocess.check_call(["pip", "install", "duckduckgo-search"])
    from duckduckgo_search import DDGS


def search_topic(query: str, max_results: int = 5, region: str = "cn-zh") -> list:
    """
    Search DuckDuckGo for a given query.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
        region: Region code (cn-zh for Chinese, wt-wt for global)
    
    Returns:
        List of search results with title, link, and snippet
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, region=region, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "link": r.get("href", ""),
                "snippet": r.get("body", "")
            })
    return results


def format_results_markdown(query: str, results: list) -> str:
    """Format search results as Markdown."""
    lines = [
        f"## 搜索结果：{query}",
        f"*检索时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        ""
    ]
    
    for i, r in enumerate(results, 1):
        lines.append(f"### {i}. [{r['title']}]({r['link']})")
        lines.append(f"> {r['snippet']}")
        lines.append("")
    
    return "\n".join(lines)


def main():
    # Define search queries related to AI education in high school + debate strategies
    queries = [
        ("高中 人工智能 课程 教育政策", "cn-zh"),
        ("AI literacy high school curriculum", "wt-wt"),
        ("普通话辩论 技巧 策略", "cn-zh"),
        ("Putonghua debate strategies tips", "wt-wt"),
    ]
    
    all_results = []
    
    print("=" * 60)
    print("普通话辩论资料检索 - DuckDuckGo Search")
    print("=" * 60)
    
    for query, region in queries:
        print(f"\n🔍 Searching: {query} (region: {region})")
        try:
            results = search_topic(query, max_results=5, region=region)
            all_results.append({
                "query": query,
                "region": region,
                "results": results
            })
            
            # Print preview
            for r in results:
                print(f"  • {r['title'][:60]}...")
                print(f"    {r['link']}")
        except Exception as e:
            print(f"  ⚠️ Error: {e}")
            all_results.append({
                "query": query,
                "region": region,
                "results": [],
                "error": str(e)
            })
    
    # Save raw JSON
    with open("search_results.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Raw results saved to search_results.json")
    
    # Generate Markdown report
    md_lines = [
        "# 普通话辩论资料检索报告",
        "",
        f"**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "**辩题**：本院主张：应在高中阶段强制设置 AI 素养必修课。",
        "",
        "---",
        ""
    ]
    
    for item in all_results:
        md_lines.append(format_results_markdown(item["query"], item["results"]))
        md_lines.append("---")
        md_lines.append("")
    
    # Add usage guide
    md_lines.extend([
        "## 资料运用建议",
        "",
        "| 来源类型 | 论证用途 |",
        "|----------|----------|",
        "| 政府/机构政策 | 界定现状、支持可行性 |",
        "| 学术研究 | 提供数据证据、因果论证 |",
        "| 教育媒体报道 | 案例分析、时效性参考 |",
        "| 博客/论坛 | 了解一线实践、反方视角 |",
        "",
        "## 下一步",
        "1. 点击链接阅读原文",
        "2. 提取关键数据与引用",
        "3. 整理到证据卡片模板",
        ""
    ])
    
    with open("demo01.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"✅ Markdown report saved to demo01.md")


if __name__ == "__main__":
    main()
