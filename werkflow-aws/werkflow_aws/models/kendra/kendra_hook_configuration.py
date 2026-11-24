from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute_condition import KendraDocumentAttributeCondition


class KendraHookConfiguration(BaseModel):
    InvocationCondition: KendraDocumentAttributeCondition | None = None
    LambdaArn: StrictStr | None = None
    S3Bucket: StrictStr | None = None
