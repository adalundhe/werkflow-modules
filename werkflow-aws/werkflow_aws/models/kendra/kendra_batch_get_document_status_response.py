from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_batch_get_document_status_response_error import KendraBatchGetDocumentStatusResponseError
from .kendra_status import KendraStatus


class KendraBatchGetDocumentStatusResponse(BaseModel):
    Errors: list[KendraBatchGetDocumentStatusResponseError] | None = None
    DocumentStatusList: list[KendraStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
