from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DeviceFarmResolution(BaseModel):
    width: StrictInt | None = None
    height: StrictInt | None = None
