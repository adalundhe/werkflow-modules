from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_attribute_condition import QBusinessDocumentAttributeCondition


class QBusinessHookConfiguration(BaseModel):
    invocationCondition: QBusinessDocumentAttributeCondition | None = None
    lambdaArn: StrictStr | None = None
    s3BucketName: StrictStr | None = None
    roleArn: StrictStr | None = None
