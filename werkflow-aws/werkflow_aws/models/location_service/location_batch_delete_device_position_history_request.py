from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationBatchDeleteDevicePositionHistoryRequest(BaseModel):
    TrackerName: StrictStr
    DeviceIds: list[StrictStr]
