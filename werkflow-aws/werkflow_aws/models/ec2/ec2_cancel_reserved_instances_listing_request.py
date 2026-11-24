from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CancelReservedInstancesListingRequest(BaseModel):
    ReservedInstancesListingId: StrictStr
