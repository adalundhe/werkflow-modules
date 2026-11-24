from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDistributionSegment(BaseModel):
    TargetCapacityTypes: list[StrictStr] | None = None
