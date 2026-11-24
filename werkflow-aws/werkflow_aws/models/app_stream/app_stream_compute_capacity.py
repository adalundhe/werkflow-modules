from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AppStreamComputeCapacity(BaseModel):
    DesiredInstances: StrictInt | None = None
    DesiredSessions: StrictInt | None = None
