from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_batch_delete_document_response_failed_document import KendraBatchDeleteDocumentResponseFailedDocument


class KendraBatchDeleteDocumentResponse(BaseModel):
    FailedDocuments: list[KendraBatchDeleteDocumentResponseFailedDocument] | None = None
    ResponseMetadata: dict[str, Any] | None = None
