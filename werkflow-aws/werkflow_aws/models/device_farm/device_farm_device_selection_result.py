from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .device_farm_device_filter import DeviceFarmDeviceFilter


class DeviceFarmDeviceSelectionResult(BaseModel):
    filters: list[DeviceFarmDeviceFilter] | None = None
    matchedDevicesCount: StrictInt | None = None
    maxDevices: StrictInt | None = None
