from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RDSServerlessV2ScalingConfigurationInfo(BaseModel):
    MinCapacity: StrictFloat | None = None
    MaxCapacity: StrictFloat | None = None
    SecondsUntilAutoPause: StrictInt | None = None
