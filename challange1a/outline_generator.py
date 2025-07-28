# outline_generator.py
import pdfplumber
from title_extractor import extract_title
from heading_detector import extract_headings

def generate_outline(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        title = extract_title(pdf)
        outline = extract_headings(pdf)

    return {
        "title": title,
        "outline": outline
    }
