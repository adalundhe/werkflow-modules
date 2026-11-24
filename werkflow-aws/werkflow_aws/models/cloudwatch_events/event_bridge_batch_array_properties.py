from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EventBridgeBatchArrayProperties(BaseModel):
    Size: StrictInt | None = None
