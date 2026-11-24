from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerDeviceStats(BaseModel):
    ConnectedDeviceCount: StrictInt | None = None
    RegisteredDeviceCount: StrictInt | None = None
