from __future__ import annotations
from pydantic import BaseModel
from .q_business_document_attribute import QBusinessDocumentAttribute


class QBusinessAttributeFilter(BaseModel):
    andAllFilters: list[QBusinessAttributeFilter] | None = None
    orAllFilters: list[QBusinessAttributeFilter] | None = None
    notFilter: QBusinessAttributeFilter | None = None
    equalsTo: QBusinessDocumentAttribute | None = None
    containsAll: QBusinessDocumentAttribute | None = None
    containsAny: QBusinessDocumentAttribute | None = None
    greaterThan: QBusinessDocumentAttribute | None = None
    greaterThanOrEquals: QBusinessDocumentAttribute | None = None
    lessThan: QBusinessDocumentAttribute | None = None
    lessThanOrEquals: QBusinessDocumentAttribute | None = None
