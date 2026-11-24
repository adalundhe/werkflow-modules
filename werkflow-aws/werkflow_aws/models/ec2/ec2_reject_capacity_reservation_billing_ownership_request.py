from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RejectCapacityReservationBillingOwnershipRequest(BaseModel):
    CapacityReservationId: StrictStr
    DryRun: StrictBool | None = None
