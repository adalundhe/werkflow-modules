from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmPurchaseOfferingRequest(BaseModel):
    offeringId: StrictStr
    quantity: StrictInt
    offeringPromotionId: StrictStr | None = None
