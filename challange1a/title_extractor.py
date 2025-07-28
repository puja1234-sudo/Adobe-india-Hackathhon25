import pdfplumber

def extract_title(pdf):
    first_page = pdf.pages[0]
    words = first_page.extract_words(use_text_flow=True, keep_blank_chars=False)
    if not words:
        return "Untitled Document"

    lines = first_page.extract_text_lines()
    if lines:
        top_line = sorted(lines, key=lambda l: -l['size'])[0]
        return top_line['text']
    return "Untitled Document"
