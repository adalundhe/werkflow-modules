from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2TargetCapacitySpecificationRequest(BaseModel):
    TotalTargetCapacity: StrictInt
    OnDemandTargetCapacity: StrictInt | None = None
    SpotTargetCapacity: StrictInt | None = None
    DefaultTargetCapacityType: Literal['spot', 'on-demand', 'capacity-block', 'reserved-capacity'] | None = None
    TargetCapacityUnitType: Literal['vcpu', 'memory-mib', 'units'] | None = None
