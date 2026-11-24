from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_device_filter import DeviceFarmDeviceFilter


class DeviceFarmListDevicesRequest(BaseModel):
    arn: StrictStr | None = None
    nextToken: StrictStr | None = None
    filters: list[DeviceFarmDeviceFilter] | None = None
