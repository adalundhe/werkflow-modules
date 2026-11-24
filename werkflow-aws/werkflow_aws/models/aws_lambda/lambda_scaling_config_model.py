from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaScalingConfigModel(BaseModel):
    MaximumConcurrency: StrictInt | None = None
