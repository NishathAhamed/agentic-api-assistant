from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ExtractedDoc:
    text: str
    pages: Optional[int]
    filetype: str
    warnings: List[str]
