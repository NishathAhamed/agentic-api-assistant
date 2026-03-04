import docx
from .models import ExtractedDoc

def read_docx(file_path):

    doc = docx.Document(file_path)

    text = "\n".join(p.text for p in doc.paragraphs)

    return ExtractedDoc(
        text=text,
        pages=len(doc),
        filetype="docx",
        warnings=[]
    )