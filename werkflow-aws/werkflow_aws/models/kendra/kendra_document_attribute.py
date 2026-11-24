from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute_value import KendraDocumentAttributeValue


class KendraDocumentAttribute(BaseModel):
    Key: StrictStr | None = None
    Value: KendraDocumentAttributeValue | None = None
