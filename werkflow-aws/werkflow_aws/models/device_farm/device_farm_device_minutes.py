from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DeviceFarmDeviceMinutes(BaseModel):
    total: StrictFloat | StrictInt | None = None
    metered: StrictFloat | StrictInt | None = None
    unmetered: StrictFloat | StrictInt | None = None
