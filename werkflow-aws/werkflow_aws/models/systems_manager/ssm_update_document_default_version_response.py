from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_document_default_version_description import SSMDocumentDefaultVersionDescription


class SSMUpdateDocumentDefaultVersionResponse(BaseModel):
    Description: SSMDocumentDefaultVersionDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
