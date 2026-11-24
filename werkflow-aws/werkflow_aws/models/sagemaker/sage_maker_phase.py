from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerPhase(BaseModel):
    InitialNumberOfUsers: StrictInt | None = None
    SpawnRate: StrictInt | None = None
    DurationInSeconds: StrictInt | None = None
