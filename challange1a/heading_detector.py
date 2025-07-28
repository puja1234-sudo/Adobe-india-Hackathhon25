# heading_detector.py
import pdfplumber
import numpy as np
from collections import defaultdict

def extract_headings_from_pdf(file_path):
    headings = []
    all_font_sizes = []

    # Step 1: Collect all font sizes from all pages
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            chars = getattr(page, "chars", [])
            if not isinstance(chars, list):
                print(f"⚠️ Skipping page {page_num} in {file_path}: Invalid chars structure.")
                continue
            for char in chars:
                size = char.get("size", 0)
                if size > 0:
                    all_font_sizes.append(size)

    if not all_font_sizes:
        print("❌ No text found in PDF.")
        return []

    # Step 2: Identify top 3 font sizes as potential heading levels
    unique_sizes = sorted(set(all_font_sizes), reverse=True)
    top_sizes = unique_sizes[:3]
    size_to_level = {size: f"H{i+1}" for i, size in enumerate(top_sizes)}
    print(f"🔍 Top heading font sizes: {top_sizes}")

    # Step 3: Process again, group by line (top), and assign heading levels
    with pdfplumber.open(file_path) as pdf:
        line_map = defaultdict(lambda: {"text": "", "font_size": 0})
        for page_num, page in enumerate(pdf.pages, start=1):
            chars = getattr(page, "chars", [])
            if not isinstance(chars, list):
                print(f"⚠️ Skipping page {page_num} in {file_path}: Invalid chars structure.")
                continue

            for char in chars:
                font_size = char.get("size", 0)
                text = char.get("text", "")
                top = round(char.get("top", 0), 1)

                key = (page_num, top)
                line_map[key]["text"] += text
                if font_size > line_map[key]["font_size"]:
                    line_map[key]["font_size"] = font_size

        for (page_num, _), value in line_map.items():
            text = value["text"].strip()
            font_size = value["font_size"]
            if font_size in top_sizes and len(text.split()) <= 15:
                headings.append({
                    "text": text,
                    "page": page_num,
                    "font_size": font_size,
                    "heading_level": size_to_level[font_size]
                })

    return headings
