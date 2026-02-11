#!/usr/bin/env python3
"""
Create two-sided answer sheet PDF with centered lines.
Tasks: 1) Move lines to centre  2) Duplicate for two-sided printing
"""
import os
import sys
from pathlib import Path

# Add process.log updates
def log(msg):
    log_path = Path(__file__).parent / "process.log"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

def main():
    base = Path(__file__).parent
    parent = base.parent
    # Prefer local copy, else parent folder
    input_pdf = base / "one-side-answer-sheet.pdf"
    if not input_pdf.exists():
        input_pdf = parent / "one-side-answer-sheet.pdf"
    output_pdf = base / "two-side-answer-sheet.pdf"
    
    log(f"[INFO] Input: {input_pdf}")
    log(f"[INFO] Output: {output_pdf}")
    
    try:
        import fitz  # PyMuPDF
        from PIL import Image
        import io
    except ImportError as e:
        log(f"[ERROR] Missing dependency: {e}")
        log("[INFO] Install with: pip install pymupdf pillow")
        sys.exit(1)
    
    # Step 1: Open and render PDF
    log("[STEP 1] Opening PDF and rendering to image...")
    doc = fitz.open(input_pdf)
    page = doc[0]
    page_rect = page.rect  # Store before closing
    # 2x resolution for quality
    mat = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    doc.close()
    
    # Convert to PIL
    img_data = pix.tobytes("png")
    pil_img = Image.open(io.BytesIO(img_data)).convert("RGB")
    w, h = pil_img.size
    log(f"[INFO] Rendered size: {w} x {h} px")
    
    # Step 2: Find content bounds; use LEFT margin for both sides (equal margins)
    log("[STEP 2] Finding content bounds and left margin...")
    import numpy as np
    arr = np.array(pil_img)
    non_white = np.any(arr < 250, axis=2)
    rows = np.any(non_white, axis=1)
    cols = np.any(non_white, axis=0)
    if not np.any(rows) or not np.any(cols):
        log("[WARN] No non-white content found, using full page")
        y_min, y_max = 0, h
        x_min, x_max = 0, w
    else:
        y_min, y_max = np.where(rows)[0][[0, -1]]
        x_min, x_max = np.where(cols)[0][[0, -1]]
    
    left_margin = int(x_min)
    # Equal margins: both sides = left_margin, so content width = w - 2*left_margin
    content_w = w - 2 * left_margin
    content_h = y_max - y_min + 1
    paste_x = left_margin
    paste_y = (h - content_h) // 2
    log(f"[INFO] Left margin (use for both): {left_margin} px")
    log(f"[INFO] Content width for equal margins: {content_w} px")
    log(f"[INFO] Paste position: ({paste_x}, {paste_y})")
    
    # Create white canvas and paste content with equal left/right margins
    centered = Image.new("RGB", (w, h), (255, 255, 255))
    crop = pil_img.crop((x_min, y_min, x_min + content_w, y_max + 1))
    centered.paste(crop, (paste_x, paste_y))
    
    # Remove page number "8" from bottom-right (it sits ~200px from right/bottom edges)
    from PIL import ImageDraw
    corner_size = 220  # px from right and bottom to fully cover the "8"
    draw = ImageDraw.Draw(centered)
    draw.rectangle([w - corner_size, h - corner_size, w, h], fill=(255, 255, 255))
    log(f"[INFO] Removed corner page number (whited out {corner_size}x{corner_size} px)")
    
    # Save centered single page for debugging
    centered.save(base / "centered_page.png")
    log("[INFO] Saved centered_page.png for verification")
    
    # Step 4: Convert to PDF and duplicate for two-sided
    log("[STEP 4] Creating two-page PDF...")
    pdf_doc = fitz.open()
    
    # Convert PIL to pixmap for fitz
    img_bytes = io.BytesIO()
    centered.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    
    # Add page 1
    rect = fitz.Rect(0, 0, page_rect.width, page_rect.height)
    pdf_page1 = pdf_doc.new_page(width=rect.width, height=rect.height)
    pdf_page1.insert_image(rect, stream=img_bytes.getvalue())
    
    # Add page 2 (duplicate)
    img_bytes.seek(0)
    pdf_page2 = pdf_doc.new_page(width=rect.width, height=rect.height)
    pdf_page2.insert_image(rect, stream=img_bytes.getvalue())
    
    pdf_doc.save(output_pdf)
    pdf_doc.close()
    
    log(f"[SUCCESS] Output saved: {output_pdf}")
    log("[DONE] Process completed.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
