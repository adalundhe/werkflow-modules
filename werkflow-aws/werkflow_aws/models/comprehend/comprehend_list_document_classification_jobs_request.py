from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_document_classification_job_filter import ComprehendDocumentClassificationJobFilter


class ComprehendListDocumentClassificationJobsRequest(BaseModel):
    Filter: ComprehendDocumentClassificationJobFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
