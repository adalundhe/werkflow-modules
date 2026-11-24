from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDisableMetricsCollectionRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    Metrics: list[StrictStr] | None = None
