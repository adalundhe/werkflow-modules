from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerRetryStrategy(BaseModel):
    MaximumRetryAttempts: StrictInt | None = None
