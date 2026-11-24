from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_document_version_info import SSMDocumentVersionInfo


class SSMListDocumentVersionsResponse(BaseModel):
    DocumentVersions: list[SSMDocumentVersionInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
