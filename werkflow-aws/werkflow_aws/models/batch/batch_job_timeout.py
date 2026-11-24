from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchJobTimeout(BaseModel):
    attemptDurationSeconds: StrictInt | None = None
