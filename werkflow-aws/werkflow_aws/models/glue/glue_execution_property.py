from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueExecutionProperty(BaseModel):
    MaxConcurrentRuns: StrictInt | None = None
