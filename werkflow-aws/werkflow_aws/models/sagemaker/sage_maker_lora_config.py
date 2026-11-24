from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerLoraConfig(BaseModel):
    Rank: StrictInt | None = None
    Alpha: StrictInt | None = None
