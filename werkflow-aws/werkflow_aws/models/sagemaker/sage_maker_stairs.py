from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerStairs(BaseModel):
    DurationInSeconds: StrictInt | None = None
    NumberOfSteps: StrictInt | None = None
    UsersPerStep: StrictInt | None = None
