from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_document_reviews import SSMDocumentReviews


class SSMUpdateDocumentMetadataRequest(BaseModel):
    Name: StrictStr
    DocumentReviews: SSMDocumentReviews
    DocumentVersion: StrictStr | None = None
