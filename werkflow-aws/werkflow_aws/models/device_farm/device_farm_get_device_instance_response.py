from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_device_instance import DeviceFarmDeviceInstance


class DeviceFarmGetDeviceInstanceResponse(BaseModel):
    deviceInstance: DeviceFarmDeviceInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
