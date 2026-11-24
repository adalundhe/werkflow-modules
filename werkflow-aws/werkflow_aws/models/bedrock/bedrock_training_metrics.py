from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class BedrockTrainingMetrics(BaseModel):
    trainingLoss: StrictFloat | StrictInt | None = None
