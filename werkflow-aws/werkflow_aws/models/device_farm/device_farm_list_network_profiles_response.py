from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_network_profile import DeviceFarmNetworkProfile


class DeviceFarmListNetworkProfilesResponse(BaseModel):
    networkProfiles: list[DeviceFarmNetworkProfile] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
