from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_block import TextractBlock
from .textract_document_metadata import TextractDocumentMetadata
from .textract_warning import TextractWarning


class TextractGetDocumentTextDetectionResponse(BaseModel):
    DocumentMetadata: TextractDocumentMetadata | None = None
    JobStatus: StrictStr | None = None
    NextToken: StrictStr | None = None
    Blocks: list[TextractBlock] | None = None
    Warnings: list[TextractWarning] | None = None
    StatusMessage: StrictStr | None = None
    DetectDocumentTextModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
