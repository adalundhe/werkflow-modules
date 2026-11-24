from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_attribute_condition import QBusinessDocumentAttributeCondition
from .q_business_document_attribute_target import QBusinessDocumentAttributeTarget


class QBusinessInlineDocumentEnrichmentConfiguration(BaseModel):
    condition: QBusinessDocumentAttributeCondition | None = None
    target: QBusinessDocumentAttributeTarget | None = None
    documentContentOperator: StrictStr | None = None
