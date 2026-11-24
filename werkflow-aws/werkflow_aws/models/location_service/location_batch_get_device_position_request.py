from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationBatchGetDevicePositionRequest(BaseModel):
    TrackerName: StrictStr
    DeviceIds: list[StrictStr]
