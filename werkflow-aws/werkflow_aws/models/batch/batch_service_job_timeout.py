from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchServiceJobTimeout(BaseModel):
    attemptDurationSeconds: StrictInt | None = None
