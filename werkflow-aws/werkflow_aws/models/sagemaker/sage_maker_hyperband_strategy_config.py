from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerHyperbandStrategyConfig(BaseModel):
    MinResource: StrictInt | None = None
    MaxResource: StrictInt | None = None
