from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueStartingEventBatchCondition(BaseModel):
    BatchSize: StrictInt | None = None
    BatchWindow: StrictInt | None = None
