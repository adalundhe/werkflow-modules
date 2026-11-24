from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_device import DeviceFarmDevice


class DeviceFarmListDevicesResponse(BaseModel):
    devices: list[DeviceFarmDevice] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
