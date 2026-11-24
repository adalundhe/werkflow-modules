from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerResourceLimits(BaseModel):
    MaxNumberOfTrainingJobs: StrictInt | None = None
    MaxParallelTrainingJobs: StrictInt | None = None
    MaxRuntimeInSeconds: StrictInt | None = None
