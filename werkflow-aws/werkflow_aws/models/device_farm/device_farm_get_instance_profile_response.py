from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_instance_profile import DeviceFarmInstanceProfile


class DeviceFarmGetInstanceProfileResponse(BaseModel):
    instanceProfile: DeviceFarmInstanceProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
