from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RDSServerlessV2ScalingConfigurationModel(BaseModel):
    MinCapacity: StrictFloat | StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    SecondsUntilAutoPause: StrictInt | None = None
