from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_document_classification_job_properties import ComprehendDocumentClassificationJobProperties


class ComprehendDescribeDocumentClassificationJobResponse(BaseModel):
    DocumentClassificationJobProperties: ComprehendDocumentClassificationJobProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
