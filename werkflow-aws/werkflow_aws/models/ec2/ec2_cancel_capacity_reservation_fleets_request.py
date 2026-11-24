from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelCapacityReservationFleetsRequest(BaseModel):
    CapacityReservationFleetIds: list[StrictStr]
    DryRun: StrictBool | None = None
