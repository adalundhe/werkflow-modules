from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaConcurrency(BaseModel):
    ReservedConcurrentExecutions: StrictInt | None = None
