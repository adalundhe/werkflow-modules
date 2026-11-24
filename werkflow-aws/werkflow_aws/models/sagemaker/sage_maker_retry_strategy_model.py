from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerRetryStrategyModel(BaseModel):
    MaximumRetryAttempts: StrictInt | None = None
