#!/usr/bin/env python3
"""Build 4-page ExcerptsOnly PDF: p1=Article A, p2=outline+reminder for B, p3=Article B, p4=outline+reminder for A.
   For 2 sheets, 4 pages, two-sided print. No glossaries in excerpts."""
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    markdown = None

DIR = Path(__file__).resolve().parent
MD_FILE = DIR / "ExcerptsOnly.md"
HTML_FILE = DIR / "ExcerptsOnly.html"
PDF_FILE = DIR / "ExcerptsOnly.pdf"


def preprocess_md(text: str) -> str:
    text = re.sub(r"`<sup>`(\d+)`</sup>`", r"<sup>\1</sup>", text)
    return text


def md_to_html(md: str) -> str:
    md = preprocess_md(md)
    if markdown:
        return markdown.markdown(md, extensions=["tables", "nl2br"], output_format="html5")
    return f"<pre>{md}</pre>"


# Empty / near-empty backs (p2, p4) – excerpts on p1, p3
BLANK_PAGE = """
<div class="page blank-page">
  <p class="blank-label">Notes.</p>
</div>
"""

def main():
    if not MD_FILE.exists():
        print(f"Error: {MD_FILE} not found", file=sys.stderr)
        sys.exit(1)

    raw = MD_FILE.read_text(encoding="utf-8")
    # Split into Article A (incl. header/task) and Article B
    parts = re.split(r"\n## Article B", raw, maxsplit=1)
    md_page1 = parts[0].strip()  # Title, task note, Article A
    md_page3 = ("## Article B" + parts[1]).strip() if len(parts) > 1 else ""

    html_page1 = md_to_html(md_page1)
    html_page3 = md_to_html(md_page3)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Mock AWQ Practice 1 – Excerpts &amp; notes (4 pages)</title>
  <style>
    body {{ font-family: Georgia, 'Times New Roman', serif; line-height: 1.45; color: #222; margin: 0; padding: 0; }}
    .page {{ box-sizing: border-box; padding: 1.2cm; min-height: 100vh; page-break-after: always; page-break-inside: avoid; }}
    .page:last-child {{ page-break-after: auto; }}
    /* Excerpt pages: compact so Article A and Article B each fit on one page */
    .excerpt-page {{ padding: 0.9cm; }}
    .excerpt-page h1 {{ font-size: 11pt; margin-top: 0; margin-bottom: 0.3em; border-bottom: 1px solid #ccc; padding-bottom: 0.2em; }}
    .excerpt-page h2 {{ font-size: 10pt; margin-top: 0.4em; margin-bottom: 0.2em; page-break-after: avoid; }}
    .excerpt-page h3 {{ font-size: 9.5pt; margin-top: 0.35em; margin-bottom: 0.15em; page-break-after: avoid; }}
    .excerpt-page h4 {{ font-size: 9pt; page-break-after: avoid; }}
    .excerpt-page p {{ margin: 0.25em 0; font-size: 8.5pt; line-height: 1.32; }}
    .excerpt-page hr {{ margin: 0.4em 0; }}
    h1 {{ font-size: 14pt; margin-top: 0; border-bottom: 1px solid #ccc; padding-bottom: 0.3em; }}
    h2 {{ font-size: 12pt; margin-top: 0.8em; page-break-after: avoid; }}
    h3 {{ font-size: 11pt; margin-top: 0.6em; page-break-after: avoid; }}
    h4 {{ font-size: 10.5pt; page-break-after: avoid; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 0.4em 0; page-break-inside: avoid; }}
    th, td {{ border: 1px solid #999; padding: 4px 6px; text-align: left; }}
    th {{ background: #f0f0f0; }}
    p {{ margin: 0.35em 0; font-size: 10.5pt; }}
    ul {{ padding-left: 1.2em; margin: 0.4em 0; }}
    sup {{ font-size: 0.75em; }}
    hr {{ border: none; border-top: 1px solid #ccc; margin: 0.6em 0; }}
    .blank-page {{ background: #fff; }}
    .blank-label {{ font-size: 10pt; color: #bbb; margin-top: 0.5em; }}
    .template-box {{ border: 1px solid #ccc; padding: 0.5em 0.8em; margin: 0.6em 0; background: #fff; page-break-inside: avoid; }}
    .lined {{ border-bottom: 1px solid #ccc; min-height: 1.2em; margin: 0.25em 0; }}
    .reminder-list {{ font-size: 10pt; }}
    .reminder-list li {{ margin: 0.35em 0; }}
    .print-note {{ font-size: 9pt; margin-top: 1em; color: #555; }}
    @media print {{
      .page {{ min-height: 100vh; }}
    }}
  </style>
</head>
<body>
  <div class="page excerpt-page">{html_page1}</div>
  {BLANK_PAGE}
  <div class="page excerpt-page">{html_page3}</div>
  {BLANK_PAGE}
</body>
</html>
"""

    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"Wrote: {HTML_FILE}")

    # Generate PDF (Playwright preferred; then Chrome; then suggest manual print)
    pdf_done = False
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(HTML_FILE.as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(PDF_FILE),
                print_background=True,
            )
            browser.close()
        print(f"Wrote: {PDF_FILE}")
        pdf_done = True
    except Exception as e:
        print(f"Playwright PDF: {e}", file=sys.stderr)

    if not pdf_done:
        import subprocess
        for chrome in [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]:
            if not Path(chrome).exists():
                continue
            try:
                subprocess.run(
                    [
                        chrome,
                        "--headless",
                        "--disable-gpu",
                        "--no-pdf-header-footer",
                        f"--print-to-pdf={PDF_FILE}",
                        HTML_FILE.as_uri(),
                    ],
                    check=True,
                    capture_output=True,
                    timeout=30,
                )
                print(f"Wrote: {PDF_FILE}")
                pdf_done = True
            except Exception as e:
                print(f"Chrome PDF: {e}", file=sys.stderr)
            break

    if not pdf_done:
        print("PDF not generated. Open ExcerptsOnly.html in a browser and use Print → Save as PDF (2-sided, 4 pages).", file=sys.stderr)


if __name__ == "__main__":
    main()
