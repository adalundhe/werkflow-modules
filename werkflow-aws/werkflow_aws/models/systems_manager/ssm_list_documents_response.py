from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_document_identifier import SSMDocumentIdentifier


class SSMListDocumentsResponse(BaseModel):
    DocumentIdentifiers: list[SSMDocumentIdentifier] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
