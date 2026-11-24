from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AutoScalingInstanceMaintenancePolicy(BaseModel):
    MinHealthyPercentage: StrictInt | None = None
    MaxHealthyPercentage: StrictInt | None = None
