from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeBillingGroupRequest(BaseModel):
    billingGroupName: StrictStr
