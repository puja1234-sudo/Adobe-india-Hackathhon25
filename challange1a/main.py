import os
import json
from heading_detector import extract_headings_from_pdf

PDF_FOLDER = "input"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def batch_process():
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            filepath = os.path.join(PDF_FOLDER, filename)
            print(f"📄 Processing: {filename}")
            try:
                headings = extract_headings_from_pdf(filepath)

                output_path = os.path.join(OUTPUT_FOLDER, filename.replace(".pdf", ".json"))
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(headings, f, indent=2, ensure_ascii=False)

                print(f"✅ Saved to: {output_path}")
            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    # 🔄 Run batch
    batch_process()

    # 🧪 Optionally test single file
    print("\n🧪 Debug Output for file01.pdf:")
    file_path = "input/file01.pdf"
    headings = extract_headings_from_pdf(file_path)
    for h in headings:
        print(f"{h['heading_level']} | Page {h['page']} | {h['text']}")
