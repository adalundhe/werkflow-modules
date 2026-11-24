from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSNodegroupScalingConfig(BaseModel):
    minSize: StrictInt | None = None
    maxSize: StrictInt | None = None
    desiredSize: StrictInt | None = None
