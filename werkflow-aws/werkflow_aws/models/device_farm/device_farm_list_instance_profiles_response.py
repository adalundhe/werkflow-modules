from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_instance_profile import DeviceFarmInstanceProfile


class DeviceFarmListInstanceProfilesResponse(BaseModel):
    instanceProfiles: list[DeviceFarmInstanceProfile] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
