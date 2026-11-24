from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerMonitoringStoppingCondition(BaseModel):
    MaxRuntimeInSeconds: StrictInt | None = None
