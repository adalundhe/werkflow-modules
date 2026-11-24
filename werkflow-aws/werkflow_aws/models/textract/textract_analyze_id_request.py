from __future__ import annotations
from pydantic import BaseModel
from .textract_document import TextractDocument


class TextractAnalyzeIDRequest(BaseModel):
    DocumentPages: list[TextractDocument]
