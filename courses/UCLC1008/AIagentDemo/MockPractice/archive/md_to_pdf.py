#!/usr/bin/env python3
"""Convert practice1.md to HTML with print-friendly CSS, then try to generate PDF."""
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    markdown = None

def _paths(basename: str):
    parent = Path(__file__).resolve().parent
    return (
        parent / f"{basename}.md",
        parent / f"{basename}.html",
        parent / f"{basename}.pdf",
    )

# Default: practice1; optional: python3 md_to_pdf.py practice1-abridged
BASENAME = sys.argv[1].replace(".md", "") if len(sys.argv) > 1 else "practice1"
MD_FILE, HTML_FILE, PDF_FILE = _paths(BASENAME)

PRINT_CSS = """
@media print {
  body { font-size: 11pt; margin: 1.2cm; }
  h1 { font-size: 16pt; margin-top: 0; page-break-after: avoid; }
  h2 { font-size: 13pt; margin-top: 1em; page-break-after: avoid; }
  h3, h4 { font-size: 12pt; page-break-after: avoid; }
  table { page-break-inside: avoid; }
  hr { border: none; border-top: 1pt solid #ccc; margin: 1em 0; }
  .no-print { display: none; }
}
"""

def preprocess_md(text: str) -> str:
    """Allow raw <sup> tags by removing backtick escaping around them."""
    # Match `<sup>`digit`</sup>` or similar and replace with <sup>digit</sup>
    text = re.sub(r"`<sup>`(\d+)`</sup>`", r"<sup>\1</sup>", text)
    return text


def _add_page_numbers_to_pdf(pdf_path: Path) -> None:
    """Overlay 'Page x of y' at bottom center of each page. Requires PyPDF2 and reportlab."""
    try:
        from io import BytesIO
        from PyPDF2 import PdfReader, PdfWriter
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
    except ImportError:
        return
    reader = PdfReader(str(pdf_path))
    n = len(reader.pages)
    writer = PdfWriter()
    w, h = letter[0], letter[1]
    for i in range(n):
        page = reader.pages[i]
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawCentredString(w / 2, 24, f"Page {i + 1} of {n}")
        c.save()
        packet.seek(0)
        overlay = PdfReader(packet)
        page.merge_page(overlay.pages[0])
        writer.add_page(page)
    with open(pdf_path, "wb") as f:
        writer.write(f)

def main():
    if not MD_FILE.exists():
        print(f"Error: {MD_FILE} not found", file=sys.stderr)
        sys.exit(1)

    raw = MD_FILE.read_text(encoding="utf-8")
    body_md = preprocess_md(raw)

    if markdown:
        html_body = markdown.markdown(
            body_md,
            extensions=["tables", "nl2br"],
            output_format="html5",
        )
    else:
        html_body = f"<pre>{body_md}</pre>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mock AWQ – {BASENAME.replace("-", " ").title()}</title>
  <style>
    body {{ font-family: Georgia, 'Times New Roman', serif; line-height: 1.5; color: #222; max-width: 800px; margin: 0 auto; padding: 1em; }}
    h1 {{ font-size: 1.5em; border-bottom: 1px solid #ccc; padding-bottom: 0.2em; }}
    h2 {{ font-size: 1.2em; margin-top: 1em; }}
    h3 {{ font-size: 1.1em; }}
    h4 {{ font-size: 1em; }}
    table {{ border-collapse: collapse; width: 100%; margin: 0.5em 0; font-size: 0.95em; }}
    th, td {{ border: 1px solid #ccc; padding: 6px 8px; text-align: left; }}
    th {{ background: #f5f5f5; }}
    sup {{ font-size: 0.75em; }}
    hr {{ margin: 1em 0; border: none; border-top: 1px solid #ccc; }}
    ul {{ padding-left: 1.5em; }}
    p {{ margin: 0.5em 0; }}
    {PRINT_CSS}
  </style>
</head>
<body>
{html_body}
</body>
</html>
"""

    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"Wrote: {HTML_FILE}")

    # Playwright Chromium only (no system Chrome — it adds file path to footer). Custom footer = "Page x of y" only.
    pdf_done = False
    footer_html = (
        '<div style="font-size:9pt; text-align:center; width:100%;">'
        'Page <span class="pageNumber"></span> of <span class="totalPages"></span>'
        '</div>'
    )
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)  # bundled Chromium only; avoid channel="chrome"
            page = browser.new_page()
            page.goto(HTML_FILE.as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(PDF_FILE),
                display_header_footer=True,
                header_template='<div></div>',
                footer_template=footer_html,
            )
            browser.close()
        print(f"Wrote: {PDF_FILE}")
        pdf_done = True
    except Exception as e:
        print(f"Playwright PDF: {e}", file=sys.stderr)

    # Fallback: Chrome CLI with no header/footer, then add page numbers (no path ever)
    if not pdf_done:
        import subprocess
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]
        for chrome in chrome_paths:
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
                _add_page_numbers_to_pdf(PDF_FILE)
                print(f"Wrote: {PDF_FILE}")
                pdf_done = True
            except Exception as e:
                print(f"Chrome PDF: {e}", file=sys.stderr)
            break
    if not pdf_done:
        try:
            from weasyprint import HTML
            HTML(string=html).write_pdf(PDF_FILE)
            print(f"Wrote: {PDF_FILE}")
        except Exception as e:
            print(f"PDF skipped: {e}", file=sys.stderr)
            print("Open practice1.html in a browser and use Print → Save as PDF.")

if __name__ == "__main__":
    main()
