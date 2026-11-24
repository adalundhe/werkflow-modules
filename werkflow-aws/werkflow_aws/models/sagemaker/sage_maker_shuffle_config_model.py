from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerShuffleConfigModel(BaseModel):
    Seed: StrictInt | None = None
