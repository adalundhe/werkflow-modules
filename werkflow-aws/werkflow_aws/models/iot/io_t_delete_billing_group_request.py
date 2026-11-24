from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteBillingGroupRequest(BaseModel):
    billingGroupName: StrictStr
    expectedVersion: StrictInt | None = None
