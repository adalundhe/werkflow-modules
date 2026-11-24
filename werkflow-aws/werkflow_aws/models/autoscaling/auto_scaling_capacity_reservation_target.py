from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingCapacityReservationTarget(BaseModel):
    CapacityReservationIds: list[StrictStr] | None = None
    CapacityReservationResourceGroupArns: list[StrictStr] | None = None
