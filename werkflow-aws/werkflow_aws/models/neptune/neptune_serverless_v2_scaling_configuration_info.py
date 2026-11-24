from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class NeptuneServerlessV2ScalingConfigurationInfo(BaseModel):
    MinCapacity: StrictFloat | StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
