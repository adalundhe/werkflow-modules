from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_network_profile import DeviceFarmNetworkProfile


class DeviceFarmGetNetworkProfileResponse(BaseModel):
    networkProfile: DeviceFarmNetworkProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
