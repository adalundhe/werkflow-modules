from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EMRComputeLimits(BaseModel):
    UnitType: StrictStr | None = None
    MinimumCapacityUnits: StrictInt | None = None
    MaximumCapacityUnits: StrictInt | None = None
    MaximumOnDemandCapacityUnits: StrictInt | None = None
    MaximumCoreCapacityUnits: StrictInt | None = None
