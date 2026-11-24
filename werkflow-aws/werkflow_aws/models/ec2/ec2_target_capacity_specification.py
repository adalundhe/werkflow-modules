from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TargetCapacitySpecification(BaseModel):
    TotalTargetCapacity: StrictInt | None = None
    OnDemandTargetCapacity: StrictInt | None = None
    SpotTargetCapacity: StrictInt | None = None
    DefaultTargetCapacityType: StrictStr | None = None
    TargetCapacityUnitType: StrictStr | None = None
