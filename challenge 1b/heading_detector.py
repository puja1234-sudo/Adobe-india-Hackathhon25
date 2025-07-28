# heading_detector.py

def extract_headings_from_pdf(pdf_path):
    # Dummy headings for testing
    return ["Executive Summary", "Revenue Trends", "R&D Investments", "Market Positioning"]

def extract_section_text(pdf_path, headings):
    print(f"📂 Extracting sections from {pdf_path} with headings: {headings}")
    # Return dummy sections matching the headings
    return [{
        "heading": heading,
        "content": f"This is dummy content under heading: {heading}",
        "source": pdf_path
    } for heading in headings]
