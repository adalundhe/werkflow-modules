from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerTrainingProgressInfo(BaseModel):
    TotalStepCountPerEpoch: StrictInt | None = None
    CurrentStep: StrictInt | None = None
    CurrentEpoch: StrictInt | None = None
    MaxEpoch: StrictInt | None = None
