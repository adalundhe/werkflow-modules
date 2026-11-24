from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_document_classifier_properties import ComprehendDocumentClassifierProperties


class ComprehendDescribeDocumentClassifierResponse(BaseModel):
    DocumentClassifierProperties: ComprehendDocumentClassifierProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
