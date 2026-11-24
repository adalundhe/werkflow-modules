from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_document_description import SSMDocumentDescription


class SSMCreateDocumentResponse(BaseModel):
    DocumentDescription: SSMDocumentDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
