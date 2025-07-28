# section_extractor.py
import pdfplumber

def extract_section_text(pdf_path, flat_headings, context_lines=3):
    sections = []
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        for entry in flat_headings:
            page = pages[entry["page"] - 1]
            lines = page.extract_text().split("\n") if page.extract_text() else []
            title = entry["text"]
            # find the line index containing title
            try:
                idx = next(i for i,l in enumerate(lines) if title in l)
            except StopIteration:
                idx = 0
            context = lines[idx:idx + context_lines + 1]
            sections.append({
                "document": pdf_path,
                "page": entry["page"],
                "section_title": title,
                "section_text": " ".join(context)
            })
    return sections
