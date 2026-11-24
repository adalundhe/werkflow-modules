from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class AutoScalingStepAdjustment(BaseModel):
    MetricIntervalLowerBound: StrictFloat | StrictInt | None = None
    MetricIntervalUpperBound: StrictFloat | StrictInt | None = None
    ScalingAdjustment: StrictInt | None = None
