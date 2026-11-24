from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .textract_document_metadata import TextractDocumentMetadata
from .textract_expense_document import TextractExpenseDocument


class TextractAnalyzeExpenseResponse(BaseModel):
    DocumentMetadata: TextractDocumentMetadata | None = None
    ExpenseDocuments: list[TextractExpenseDocument] | None = None
    ResponseMetadata: dict[str, Any] | None = None
