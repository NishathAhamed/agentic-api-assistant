import pymupdf as fitz
from .models import ExtractedDoc

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return ExtractedDoc(
        text=text,
        pages=len(doc),
        filetype="pdf",
        warnings=[]
    )