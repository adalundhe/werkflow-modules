from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EventBridgeBatchRetryStrategy(BaseModel):
    Attempts: StrictInt | None = None
