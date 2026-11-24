from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerHyperParameterTuningJobConsumedResources(BaseModel):
    RuntimeInSeconds: StrictInt | None = None
