from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .device_farm_device import DeviceFarmDevice
from .device_farm_incompatibility_message import DeviceFarmIncompatibilityMessage


class DeviceFarmDevicePoolCompatibilityResult(BaseModel):
    device: DeviceFarmDevice | None = None
    compatible: StrictBool | None = None
    incompatibilityMessages: list[DeviceFarmIncompatibilityMessage] | None = None
