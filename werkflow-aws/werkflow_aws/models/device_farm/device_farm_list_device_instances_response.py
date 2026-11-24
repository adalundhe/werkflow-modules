from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_device_instance import DeviceFarmDeviceInstance


class DeviceFarmListDeviceInstancesResponse(BaseModel):
    deviceInstances: list[DeviceFarmDeviceInstance] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
