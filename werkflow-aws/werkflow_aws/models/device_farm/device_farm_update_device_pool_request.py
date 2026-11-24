from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .device_farm_rule import DeviceFarmRule


class DeviceFarmUpdateDevicePoolRequest(BaseModel):
    arn: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    rules: list[DeviceFarmRule] | None = None
    maxDevices: StrictInt | None = None
    clearMaxDevices: StrictBool | None = None
