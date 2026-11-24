from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DynamoDBSSESpecificationModel(BaseModel):
    Enabled: StrictBool | None = None
    SSEType: StrictStr | None = None
    KMSMasterKeyId: StrictStr | None = None
