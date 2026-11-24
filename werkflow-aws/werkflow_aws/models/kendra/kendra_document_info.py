from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute import KendraDocumentAttribute


class KendraDocumentInfo(BaseModel):
    DocumentId: StrictStr
    Attributes: list[KendraDocumentAttribute] | None = None
