from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_device_pool import DeviceFarmDevicePool


class DeviceFarmListDevicePoolsResponse(BaseModel):
    devicePools: list[DeviceFarmDevicePool] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
