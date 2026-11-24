from __future__ import annotations
from pydantic import BaseModel
from .kendra_document_attribute import KendraDocumentAttribute


class KendraAttributeFilter(BaseModel):
    AndAllFilters: list[KendraAttributeFilter] | None = None
    OrAllFilters: list[KendraAttributeFilter] | None = None
    NotFilter: KendraAttributeFilter | None = None
    EqualsTo: KendraDocumentAttribute | None = None
    ContainsAll: KendraDocumentAttribute | None = None
    ContainsAny: KendraDocumentAttribute | None = None
    GreaterThan: KendraDocumentAttribute | None = None
    GreaterThanOrEquals: KendraDocumentAttribute | None = None
    LessThan: KendraDocumentAttribute | None = None
    LessThanOrEquals: KendraDocumentAttribute | None = None
