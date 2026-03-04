from pathlib import Path
from .models import ExtractedDoc


def read_txt(file_path):

    text = Path(file_path).read_text(encoding="utf-8")

    return ExtractedDoc(
        text=text,
        pages=None,
        filetype="txt",
        warnings=[]
    )