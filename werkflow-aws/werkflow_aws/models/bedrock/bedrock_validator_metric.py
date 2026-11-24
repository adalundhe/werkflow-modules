from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class BedrockValidatorMetric(BaseModel):
    validationLoss: StrictFloat | StrictInt | None = None
