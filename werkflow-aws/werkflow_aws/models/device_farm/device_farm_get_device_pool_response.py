from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_device_pool import DeviceFarmDevicePool


class DeviceFarmGetDevicePoolResponse(BaseModel):
    devicePool: DeviceFarmDevicePool | None = None
    ResponseMetadata: dict[str, Any] | None = None
