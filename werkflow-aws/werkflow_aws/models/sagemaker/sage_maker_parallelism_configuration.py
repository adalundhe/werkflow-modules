from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerParallelismConfiguration(BaseModel):
    MaxParallelExecutionSteps: StrictInt | None = None
