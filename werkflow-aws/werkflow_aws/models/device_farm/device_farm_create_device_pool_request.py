from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .device_farm_rule import DeviceFarmRule


class DeviceFarmCreateDevicePoolRequest(BaseModel):
    projectArn: StrictStr
    name: StrictStr
    rules: list[DeviceFarmRule]
    description: StrictStr | None = None
    maxDevices: StrictInt | None = None
