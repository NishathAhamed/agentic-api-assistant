Here is a **clean updated `README.md` section with the Tech Stack properly highlighted** (including **LangGraph, Python, FastAPI, Groq, Mermaid, etc.**). This version looks **more professional for a portfolio or GitHub project**, which is useful since you mentioned you're preparing for **software engineering roles**.

You can paste this into your README.

---

# Agentic API Support – AI-Driven UML Diagram Generator

An **agentic AI system** that extracts API documentation from files and automatically generates **UML sequence diagrams**.

The system ingests documents such as **PDF, DOCX, and TXT**, extracts structured API information, and produces **validated Mermaid sequence diagrams rendered as PNG images**.

The architecture follows a **modular pipeline design** separating document ingestion, processing, reasoning, validation, and rendering.

---

# Architecture Overview

```text
Document Upload
      ↓
Document Extract Layer
      ↓
Normalization Layer
      ↓
Fact Extraction Layer
      ↓
UML Builder
      ↓
Validation Layer
      ↓
Mermaid Renderer → PNG
```

Each layer is independent, making the system **scalable, testable, and reusable**.

---

# Tech Stack

## Core

* **Python 3.11+**
* **FastAPI** – API framework for serving the UML generator
* **Pydantic** – Data validation and schema management

## Agentic AI Framework

* **LangGraph** – Multi-agent orchestration framework
* **LangChain** – LLM integration utilities
* **Groq LLM** – Fast inference for structured outputs

## Document Processing

* **PyMuPDF (fitz)** – PDF text extraction
* **python-docx** – DOCX document parsing
* **Pillow** – Image processing (future OCR support)

## Diagram Generation

* **Mermaid** – Diagram definition language
* **Mermaid CLI (mmdc)** – Rendering Mermaid diagrams to PNG

## Development Workflow

* **Jupyter Notebooks** – Iterative development and testing
* **Pytest** – Automated testing (planned)

---

# Project Structure

```text
agentic-api-support
│
├── app/
│   └── main.py                # FastAPI application entrypoint
│
├── core/
│   ├── normalize/             # API section splitting
│   ├── facts/                 # Fact extraction and storage
│   ├── uml/                   # UML sequence diagram builder
│   └── validate/              # Truth validation layer
│
├── document_extract/          # Document ingestion layer
│   ├── __init__.py
│   ├── models.py
│   ├── extractor.py
│   ├── pdf_reader.py
│   ├── docx_reader.py
│   └── txt_reader.py
│
├── assets/                    # Sample documents for testing
│
├── notebooks/                 # Development notebooks
│   └── 01_ingestion.ipynb
│
├── outputs/                   # Generated diagrams
│
└── README.md
```

---

# Document Extract Layer

The **document extraction module** converts different file types into a unified data structure.

Supported formats:

* TXT
* DOCX
* PDF

Example output structure:

```python
ExtractedDoc(
    text="document content",
    pages=5,
    filetype="pdf",
    warnings=[]
)
```

Example usage:

```python
from document_extract.extractor import extract_text

doc = extract_text("assets/sample.pdf")

print(doc.text[:500])
print(doc.filetype)
print(doc.pages)
print(doc.warnings)
```

---

# Features

* Multi-format document ingestion
* Modular architecture for extensibility
* Fact-based diagram generation
* Evidence validation for diagram accuracy
* Mermaid diagram rendering
* PNG export support
* Notebook-based development workflow

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

API available at:

```
http://localhost:8000
```

Interactive API docs:

```
http://localhost:8000/docs
```

---

# Future Improvements

* OCR support for scanned PDFs
* Multi-agent reasoning using LangGraph
* Automatic API structure detection
* Additional UML diagram types
* AI-assisted validation improvements

---

# Author

**Ahamed Nishath**

Software Engineer | AI Systems Enthusiast

GitHub
[https://github.com/NishathAhamed](https://github.com/NishathAhamed)

---

If you want, I can also help you add **two things that make this README look much more “senior engineer level”**:

1. **Architecture diagram (visual)**
2. **Example generated UML diagram image**

These make GitHub projects **look far more impressive to recruiters**.
