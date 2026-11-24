from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .kendra_document_attribute_condition import KendraDocumentAttributeCondition
from .kendra_document_attribute_target import KendraDocumentAttributeTarget


class KendraInlineCustomDocumentEnrichmentConfiguration(BaseModel):
    Condition: KendraDocumentAttributeCondition | None = None
    Target: KendraDocumentAttributeTarget | None = None
    DocumentContentDeletion: StrictBool | None = None
