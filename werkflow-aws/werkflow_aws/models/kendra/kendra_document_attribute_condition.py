from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute_value import KendraDocumentAttributeValue


class KendraDocumentAttributeCondition(BaseModel):
    ConditionDocumentAttributeKey: StrictStr | None = None
    Operator: StrictStr | None = None
    ConditionOnValue: KendraDocumentAttributeValue | None = None
