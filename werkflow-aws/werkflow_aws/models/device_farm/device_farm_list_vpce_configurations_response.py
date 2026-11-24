from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_vpce_configuration import DeviceFarmVPCEConfiguration


class DeviceFarmListVPCEConfigurationsResponse(BaseModel):
    vpceConfigurations: list[DeviceFarmVPCEConfiguration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
