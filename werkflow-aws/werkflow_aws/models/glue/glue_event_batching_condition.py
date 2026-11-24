from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueEventBatchingCondition(BaseModel):
    BatchSize: StrictInt | None = None
    BatchWindow: StrictInt | None = None
