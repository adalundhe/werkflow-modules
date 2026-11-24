from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_document_classifier_filter import ComprehendDocumentClassifierFilter


class ComprehendListDocumentClassifiersRequest(BaseModel):
    Filter: ComprehendDocumentClassifierFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
