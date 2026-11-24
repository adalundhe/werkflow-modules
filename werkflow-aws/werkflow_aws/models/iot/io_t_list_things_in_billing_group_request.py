from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListThingsInBillingGroupRequest(BaseModel):
    billingGroupName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
