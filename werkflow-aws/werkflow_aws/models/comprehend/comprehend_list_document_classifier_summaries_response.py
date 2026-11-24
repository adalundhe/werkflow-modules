from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_document_classifier_summary import ComprehendDocumentClassifierSummary


class ComprehendListDocumentClassifierSummariesResponse(BaseModel):
    DocumentClassifierSummariesList: list[ComprehendDocumentClassifierSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
