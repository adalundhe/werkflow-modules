from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerAutoMLJobCompletionCriteria(BaseModel):
    MaxCandidates: StrictInt | None = None
    MaxRuntimePerTrainingJobInSeconds: StrictInt | None = None
    MaxAutoMLJobRuntimeInSeconds: StrictInt | None = None
