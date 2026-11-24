from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .device_farm_device_filter import DeviceFarmDeviceFilter


class DeviceFarmDeviceSelectionConfiguration(BaseModel):
    filters: list[DeviceFarmDeviceFilter]
    maxDevices: StrictInt
