from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_dbsse_type import DynamoDBSSEType


class DynamoDBSSESpecification(BaseModel):
    Enabled: StrictBool | None = None
    SSEType: DynamoDBSSEType | None = None
    KMSMasterKeyId: StrictStr | None = None
