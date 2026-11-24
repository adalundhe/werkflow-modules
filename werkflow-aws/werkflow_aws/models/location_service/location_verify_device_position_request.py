from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .location_device_state import LocationDeviceState


class LocationVerifyDevicePositionRequest(BaseModel):
    TrackerName: StrictStr
    DeviceState: LocationDeviceState
    DistanceUnit: Literal['Kilometers', 'Miles'] | None = None
