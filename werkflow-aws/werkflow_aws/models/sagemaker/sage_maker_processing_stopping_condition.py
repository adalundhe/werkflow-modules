from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerProcessingStoppingCondition(BaseModel):
    MaxRuntimeInSeconds: StrictInt | None = None
