from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .device_farm_rule import DeviceFarmRule


class DeviceFarmDevicePool(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    type: StrictStr | None = None
    rules: list[DeviceFarmRule] | None = None
    maxDevices: StrictInt | None = None
