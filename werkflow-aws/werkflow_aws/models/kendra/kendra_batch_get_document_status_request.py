from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_info import KendraDocumentInfo


class KendraBatchGetDocumentStatusRequest(BaseModel):
    IndexId: StrictStr
    DocumentInfoList: list[KendraDocumentInfo]
