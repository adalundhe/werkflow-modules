from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSMemoryMiBRequest(BaseModel):
    min: StrictInt | None = None
    max: StrictInt | None = None
