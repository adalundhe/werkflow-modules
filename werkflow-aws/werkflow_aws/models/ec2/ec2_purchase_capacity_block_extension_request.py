from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2PurchaseCapacityBlockExtensionRequest(BaseModel):
    CapacityBlockExtensionOfferingId: StrictStr
    CapacityReservationId: StrictStr
    DryRun: StrictBool | None = None
