from __future__ import annotations
from pydantic import BaseModel
from .kendra_document_attribute import KendraDocumentAttribute
from .kendra_expanded_result_item import KendraExpandedResultItem


class KendraCollapsedResultDetail(BaseModel):
    DocumentAttribute: KendraDocumentAttribute | None = None
    ExpandedResults: list[KendraExpandedResultItem] | None = None
