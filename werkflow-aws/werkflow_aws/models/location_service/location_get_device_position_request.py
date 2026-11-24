from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetDevicePositionRequest(BaseModel):
    TrackerName: StrictStr
    DeviceId: StrictStr
