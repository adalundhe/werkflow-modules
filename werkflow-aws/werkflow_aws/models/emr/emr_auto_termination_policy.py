from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EMRAutoTerminationPolicy(BaseModel):
    IdleTimeout: StrictInt | None = None
