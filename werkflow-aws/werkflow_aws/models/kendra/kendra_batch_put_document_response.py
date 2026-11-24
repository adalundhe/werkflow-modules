from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_batch_put_document_response_failed_document import KendraBatchPutDocumentResponseFailedDocument


class KendraBatchPutDocumentResponse(BaseModel):
    FailedDocuments: list[KendraBatchPutDocumentResponseFailedDocument] | None = None
    ResponseMetadata: dict[str, Any] | None = None
