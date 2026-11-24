from __future__ import annotations
from pydantic import BaseModel
from .textract_document import TextractDocument


class TextractDetectDocumentTextRequest(BaseModel):
    Document: TextractDocument
