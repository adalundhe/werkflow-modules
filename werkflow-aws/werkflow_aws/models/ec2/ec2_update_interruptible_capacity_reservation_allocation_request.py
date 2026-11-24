from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2UpdateInterruptibleCapacityReservationAllocationRequest(BaseModel):
    CapacityReservationId: StrictStr
    TargetInstanceCount: StrictInt | None = None
    DryRun: StrictBool | None = None
    ZeroSizePreference: Literal['retain', 'default'] | None = None
