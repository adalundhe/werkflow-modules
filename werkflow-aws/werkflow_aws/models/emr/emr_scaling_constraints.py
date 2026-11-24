from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EMRScalingConstraints(BaseModel):
    MinCapacity: StrictInt | None = None
    MaxCapacity: StrictInt | None = None
