from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteQueuedReservedInstancesRequest(BaseModel):
    ReservedInstancesIds: list[StrictStr]
    DryRun: StrictBool | None = None
