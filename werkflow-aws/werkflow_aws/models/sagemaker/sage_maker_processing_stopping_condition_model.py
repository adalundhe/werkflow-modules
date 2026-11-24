from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerProcessingStoppingConditionModel(BaseModel):
    MaxRuntimeInSeconds: StrictInt | None = None
