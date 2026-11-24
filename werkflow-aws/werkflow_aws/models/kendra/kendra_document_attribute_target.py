from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_document_attribute_value import KendraDocumentAttributeValue


class KendraDocumentAttributeTarget(BaseModel):
    TargetDocumentAttributeKey: StrictStr | None = None
    TargetDocumentAttributeValueDeletion: StrictBool | None = None
    TargetDocumentAttributeValue: KendraDocumentAttributeValue | None = None
