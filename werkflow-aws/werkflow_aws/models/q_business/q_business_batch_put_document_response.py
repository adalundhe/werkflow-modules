from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .q_business_failed_document import QBusinessFailedDocument


class QBusinessBatchPutDocumentResponse(BaseModel):
    failedDocuments: list[QBusinessFailedDocument] | None = None
    ResponseMetadata: dict[str, Any] | None = None
