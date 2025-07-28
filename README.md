
# 📘1a) PDF Heading Extractor – Adobe India Hackathon 2025

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



# 📘 PDF Persona-Based Section Ranker – Adobe India Hackathon 2025 (Challenge 1b)

This project extracts and ranks relevant sections from multiple PDF documents based on a given **persona** and a **job-to-be-done**. It simulates a personalized document summarization system using dummy heading and ranking logic.

---

## 🚀 Features

- 📄 Extracts dummy headings from PDFs  
- 🧠 Scores sections based on persona & job  
- 🧩 Merges multiple documents into a single ranked JSON  
- 🐳 Dockerized for easy deployment  

---

## 📁 Project Structure

```
challange1b/
├── input/                              # Input folder
│   ├── docs/                           # Folder containing input PDFs
│   │   ├── file01.pdf
│   │   ├── file02.pdf
│   │   ├── file03.pdf
│   │   ├── file04.pdf
│   │   └── file05.pdf
│   └── persona.json                    # Input persona and job-to-be-done
├── output/                             # Output result.json will be written here
├── main_1b.py                          # Main pipeline script
├── heading_detector.py                # Dummy heading and section extractor
├── ranker.py                           # Scores sections based on persona
├── section_extractor.py               # Extracts section content from PDF
├── outline_builder.py                 # Builds hierarchical outline (not used here)
├── Dockerfile                          # Docker container setup
└── README.md                           # You're here!
```

---

## 📦 Requirements

- Python 3.10+
- Libraries:
  - `pdfplumber`

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🐍 Run Locally

1. Place your PDF files inside `input/docs/`.
2. Create a `persona.json` file inside `input/` like below:

```json
{
  "persona": "Product Manager at Adobe",
  "job_to_be_done": "Understand recent revenue trends in tech"
}
```

3. Run the script:

```bash
python main_1b.py
```

4. Output will be saved to `output/result.json`.

---

## 🐳 Run with Docker

### 🔨 Build Docker Image:

```bash
docker build -t persona-section-ranker .
```

### ▶️ Run Docker Container:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output persona-section-ranker
```

> 💡 On Windows, replace `$(pwd)` with full absolute path.

---

## 🧪 Sample Output

```json
{
  "metadata": {
    "documents": ["file01.pdf", "file02.pdf"],
    "persona": "Product Manager at Adobe",
    "job_to_be_done": "Understand recent revenue trends in tech",
    "timestamp": "2025-07-28T18:30:00"
  },
  "sections": [
    {
      "heading": "Revenue Trends",
      "content": "This is dummy content under heading: Revenue Trends",
      "source": "input/docs/file01.pdf",
      "score": 1.0
    }
  ]
}
```

---

## 🧠 Modules Explained

| File                   | Purpose                                                  |
|------------------------|-----------------------------------------------------------|
| `main_1b.py`           | Entry point: ties everything together                     |
| `heading_detector.py`  | Dummy heading extractor & section fetcher                |
| `ranker.py`            | Scores each section with dummy score                     |
| `section_extractor.py` | Gets nearby content for a heading from PDF               |
| `outline_builder.py`   | Builds hierarchy of headings (not used in 1b directly)   |
| `Dockerfile`           | Makes the project portable via container                 |

---

## 👥 Contributors

- [puja1234-sudo](https://github.com/puja1234-sudo)
- [Avanish-22](https://github.com/Avanish-22)

---

## 📄 License

This repository is intended for learning and Adobe Hackathon use only.

---

## 💬 Feedback

Suggestions or improvements? Feel free to open an issue or pull request.
