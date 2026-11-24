from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerBestObjectiveNotImproving(BaseModel):
    MaxNumberOfTrainingJobsNotImproving: StrictInt | None = None
