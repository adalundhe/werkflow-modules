from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2MemoryMiB(BaseModel):
    Min: StrictInt | None = None
    Max: StrictInt | None = None
