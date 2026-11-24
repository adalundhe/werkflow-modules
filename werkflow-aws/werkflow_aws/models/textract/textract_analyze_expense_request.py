from __future__ import annotations
from pydantic import BaseModel
from .textract_document import TextractDocument


class TextractAnalyzeExpenseRequest(BaseModel):
    Document: TextractDocument
