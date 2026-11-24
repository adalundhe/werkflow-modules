from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_document_metadata_response_info import SSMDocumentMetadataResponseInfo


class SSMListDocumentMetadataHistoryResponse(BaseModel):
    Name: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Author: StrictStr | None = None
    Metadata: SSMDocumentMetadataResponseInfo | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
