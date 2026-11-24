from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_attribute_value import QBusinessDocumentAttributeValue


class QBusinessDocumentAttributeCondition(BaseModel):
    key: StrictStr | None = None
    operator: StrictStr | None = None
    value: QBusinessDocumentAttributeValue | None = None
