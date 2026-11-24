from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_device_pool_compatibility_result import DeviceFarmDevicePoolCompatibilityResult


class DeviceFarmGetDevicePoolCompatibilityResponse(BaseModel):
    compatibleDevices: list[DeviceFarmDevicePoolCompatibilityResult] | None = None
    incompatibleDevices: list[DeviceFarmDevicePoolCompatibilityResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
