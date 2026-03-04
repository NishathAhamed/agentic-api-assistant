from pathlib import Path

from .pdf_reader import read_pdf
from .docx_reader import read_docx
from .txt_reader import read_txt


def extract_text(file_path: str):

    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return read_pdf(file_path)

    if suffix == ".docx":
        return read_docx(file_path)

    if suffix == ".txt":
        return read_txt(file_path)

    raise ValueError(f"Unsupported file type: {suffix}")