from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_document_metadata import TextractDocumentMetadata
from .textract_expense_document import TextractExpenseDocument
from .textract_warning import TextractWarning


class TextractGetExpenseAnalysisResponse(BaseModel):
    DocumentMetadata: TextractDocumentMetadata | None = None
    JobStatus: StrictStr | None = None
    NextToken: StrictStr | None = None
    ExpenseDocuments: list[TextractExpenseDocument] | None = None
    Warnings: list[TextractWarning] | None = None
    StatusMessage: StrictStr | None = None
    AnalyzeExpenseModelVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
