from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchComputeScalingPolicy(BaseModel):
    minScaleDownDelayMinutes: StrictInt | None = None
