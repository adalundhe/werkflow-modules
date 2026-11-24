from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .kendra_document_attribute_value import KendraDocumentAttributeValue
from .kendra_facet_result import KendraFacetResult


class KendraDocumentAttributeValueCountPair(BaseModel):
    DocumentAttributeValue: KendraDocumentAttributeValue | None = None
    Count: StrictInt | None = None
    FacetResults: list[KendraFacetResult] | None = None
