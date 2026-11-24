from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DocumentDBServerlessV2ScalingConfiguration(BaseModel):
    MinCapacity: StrictFloat | StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
