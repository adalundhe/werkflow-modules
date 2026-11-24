from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_block import TextractBlock
from .textract_document_metadata import TextractDocumentMetadata


class TextractDetectDocumentTextResponse(BaseModel):
    DocumentMetadata: TextractDocumentMetadata | None = None
    Blocks: list[TextractBlock] | None = None
    DetectDocumentTextModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
