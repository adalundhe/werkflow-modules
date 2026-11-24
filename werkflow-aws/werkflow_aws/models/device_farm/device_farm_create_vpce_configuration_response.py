from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_vpce_configuration import DeviceFarmVPCEConfiguration


class DeviceFarmCreateVPCEConfigurationResponse(BaseModel):
    vpceConfiguration: DeviceFarmVPCEConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
