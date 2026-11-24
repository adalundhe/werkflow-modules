from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute import KendraDocumentAttribute


class KendraSourceDocument(BaseModel):
    DocumentId: StrictStr | None = None
    SuggestionAttributes: list[StrictStr] | None = None
    AdditionalAttributes: list[KendraDocumentAttribute] | None = None
