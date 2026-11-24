from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchArrayProperties(BaseModel):
    size: StrictInt | None = None
