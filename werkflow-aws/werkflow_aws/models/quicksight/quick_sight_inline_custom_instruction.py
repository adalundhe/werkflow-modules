from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_uploaded_document_metadata import QuickSightUploadedDocumentMetadata


class QuickSightInlineCustomInstruction(BaseModel):
    InstructionText: StrictStr | None = None
    UploadedDocumentMetadata: QuickSightUploadedDocumentMetadata | None = None
