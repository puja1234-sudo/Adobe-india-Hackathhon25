# main.py

import os, json, time
from heading_detector import extract_headings_from_pdf, extract_section_text
from ranker import score_sections

INPUT_DOCS = "input/docs"
PERSONA_FILE = "input/persona.json"
OUTPUT_FILE = "output/result.json"

def main():
    with open(PERSONA_FILE, "r", encoding="utf-8") as f:
        persona_json = json.load(f)
    persona = persona_json.get("persona", "")
    job = persona_json.get("job_to_be_done", "")

    print("🧑‍💼 Persona:", persona)
    print("🎯 Job:", job)

    all_sections = []
    flat_headings = {}

    if not os.path.exists(INPUT_DOCS):
        print(f"❌ Input folder '{INPUT_DOCS}' not found!")
        return

    for fname in os.listdir(INPUT_DOCS):
        if fname.lower().endswith(".pdf"):
            print(f"📄 Found PDF: {fname}")
            path = os.path.join(INPUT_DOCS, fname)
            headings = extract_headings_from_pdf(path)
            print(f"🔍 Headings extracted: {headings}")
            flat_headings[fname] = headings

            secs = extract_section_text(path, headings)
            print(f"🧩 Sections extracted: {len(secs)}")
            all_sections.extend(secs)

    if not all_sections:
        print("⚠️ No sections extracted from documents. Exiting.")
        return

    ranked = score_sections(all_sections, persona_json, job)

    result = {
        "metadata": {
            "documents": list(flat_headings.keys()),
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        },
        "sections": ranked
    }

    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("✅ Output written to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
