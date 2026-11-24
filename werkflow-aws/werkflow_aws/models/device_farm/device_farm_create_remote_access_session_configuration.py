from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .device_farm_device_proxy import DeviceFarmDeviceProxy


class DeviceFarmCreateRemoteAccessSessionConfiguration(BaseModel):
    auxiliaryApps: list[StrictStr] | None = None
    billingMethod: Literal['METERED', 'UNMETERED'] | None = None
    vpceConfigurationArns: list[StrictStr] | None = None
    deviceProxy: DeviceFarmDeviceProxy | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
