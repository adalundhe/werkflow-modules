from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerParallelismConfigurationModel(BaseModel):
    MaxParallelExecutionSteps: StrictInt | None = None
