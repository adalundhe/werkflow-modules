from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_document_metadata import TextractDocumentMetadata
from .textract_lending_result import TextractLendingResult
from .textract_warning import TextractWarning


class TextractGetLendingAnalysisResponse(BaseModel):
    DocumentMetadata: TextractDocumentMetadata | None = None
    JobStatus: StrictStr | None = None
    NextToken: StrictStr | None = None
    Results: list[TextractLendingResult] | None = None
    Warnings: list[TextractWarning] | None = None
    StatusMessage: StrictStr | None = None
    AnalyzeLendingModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
