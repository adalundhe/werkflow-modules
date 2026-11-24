from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DeviceFarmTrialMinutes(BaseModel):
    total: StrictFloat | StrictInt | None = None
    remaining: StrictFloat | StrictInt | None = None
