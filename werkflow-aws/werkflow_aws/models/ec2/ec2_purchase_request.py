from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2PurchaseRequest(BaseModel):
    InstanceCount: StrictInt
    PurchaseToken: StrictStr
