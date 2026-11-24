from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingEnableMetricsCollectionRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    Granularity: StrictStr
    Metrics: list[StrictStr] | None = None
