
# 📘 PDF Heading Extractor – Adobe India Hackathon 2025

This project automates the extraction of headings from PDF documents based on font sizes. Designed for the **Adobe India Hackathon**, it identifies headings (H1, H2, H3) by analyzing font properties using `pdfplumber`, and outputs structured JSON for each file.

---

## 🚀 Features

- 📄 Batch-process multiple PDFs
- 🔠 Detect headings based on top font sizes
- 🔎 Extract titles and outlines
- 🧪 Debug-friendly logs
- 🐳 Docker-ready deployment

---

## 📁 Project Structure

```
challange1a/
├── input/                 # Folder containing input PDF files
│   ├── file01.pdf
│   ├── file02.pdf
│   ├── file03.pdf
│   ├── file04.pdf
│   └── file05.pdf
├── output/                # Generated JSON files will appear here
├── main.py                # Batch processor script
├── heading_detector.py    # Extracts headings using font sizes
├── title_extractor.py     # Extracts document title
├── outline_generator.py   # Combines title and heading extraction
├── Dockerfile             # Container setup
└── README.md              # You're here!
```



---

## 🛠️ Requirements

- Python 3.10+
- Libraries:
  - `pdfplumber`
  - `numpy`

You can install them with:

```bash
pip install -r requirements.txt

🐍 How to Run (Locally)
Place your PDF files inside the input/ folder.

Run the main script:
python main.py

Output .json files will be saved in the output/ folder.

🐳 How to Run with Docker
Build the Docker Image:
docker build -t pdf-heading-extractor .

Run the Container:
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-heading-extractor

🧪 Sample Output
[
  {
    "text": "Introduction",
    "page": 1,
    "font_size": 24.0,
    "heading_level": "H1"
  },
  {
    "text": "Getting Started",
    "page": 2,
    "font_size": 18.0,
    "heading_level": "H2"
  }
]

📂 Modules Overview
| File                   | Description                             |
| ---------------------- | --------------------------------------- |
| `main.py`              | Main driver to process PDFs in batch    |
| `heading_detector.py`  | Extracts headings using font size logic |
| `title_extractor.py`   | Extracts main title from the first page |
| `outline_generator.py` | Generates a structured outline          |
| `Dockerfile`           | Builds a container to run the extractor |

👥 Contributors

- [puja1234-sudo](https://github.com/puja1234-sudo)
- [Avanish-22](https://github.com/Avanish-22)


📃 License
This project is intended for educational and hackathon purposes only.

💬 Feedback
Found an issue or have a suggestion? Feel free to open an issue or reach out on GitHub!





