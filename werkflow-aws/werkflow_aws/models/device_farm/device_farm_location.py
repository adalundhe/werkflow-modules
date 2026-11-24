from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DeviceFarmLocation(BaseModel):
    latitude: StrictFloat | StrictInt | None = None
    longitude: StrictFloat | StrictInt | None = None
