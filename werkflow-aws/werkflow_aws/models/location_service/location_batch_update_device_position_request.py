from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .location_device_position_update import LocationDevicePositionUpdate


class LocationBatchUpdateDevicePositionRequest(BaseModel):
    TrackerName: StrictStr
    Updates: list[LocationDevicePositionUpdate]
