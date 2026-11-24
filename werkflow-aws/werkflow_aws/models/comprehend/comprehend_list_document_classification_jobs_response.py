from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_document_classification_job_properties import ComprehendDocumentClassificationJobProperties


class ComprehendListDocumentClassificationJobsResponse(BaseModel):
    DocumentClassificationJobPropertiesList: list[ComprehendDocumentClassificationJobProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
