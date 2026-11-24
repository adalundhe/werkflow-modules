from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_document_metadata import TextractDocumentMetadata
from .textract_identity_document import TextractIdentityDocument


class TextractAnalyzeIDResponse(BaseModel):
    IdentityDocuments: list[TextractIdentityDocument] | None = None
    DocumentMetadata: TextractDocumentMetadata | None = None
    AnalyzeIDModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
