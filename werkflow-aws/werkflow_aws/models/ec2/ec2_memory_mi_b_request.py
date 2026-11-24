from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2MemoryMiBRequest(BaseModel):
    Min: StrictInt | None = None
    Max: StrictInt | None = None
