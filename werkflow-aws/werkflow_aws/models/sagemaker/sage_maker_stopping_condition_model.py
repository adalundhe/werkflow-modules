from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerStoppingConditionModel(BaseModel):
    MaxRuntimeInSeconds: StrictInt | None = None
    MaxWaitTimeInSeconds: StrictInt | None = None
    MaxPendingTimeInSeconds: StrictInt | None = None
