from __future__ import annotations
from pydantic import BaseModel
from .ssm_document_reviewer_response_source import SSMDocumentReviewerResponseSource


class SSMDocumentMetadataResponseInfo(BaseModel):
    ReviewerResponse: list[SSMDocumentReviewerResponseSource] | None = None
