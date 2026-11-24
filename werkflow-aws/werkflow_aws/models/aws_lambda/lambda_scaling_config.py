from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaScalingConfig(BaseModel):
    MaximumConcurrency: StrictInt | None = None
