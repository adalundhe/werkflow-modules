from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmRenewOfferingRequest(BaseModel):
    offeringId: StrictStr
    quantity: StrictInt
