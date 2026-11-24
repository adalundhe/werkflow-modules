from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerShuffleConfig(BaseModel):
    Seed: StrictInt | None = None
