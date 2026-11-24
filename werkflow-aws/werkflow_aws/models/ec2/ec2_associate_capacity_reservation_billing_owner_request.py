from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateCapacityReservationBillingOwnerRequest(BaseModel):
    CapacityReservationId: StrictStr
    UnusedReservationBillingOwnerId: StrictStr
    DryRun: StrictBool | None = None
