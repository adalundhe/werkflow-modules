from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_device import NetworkManagerDevice


class NetworkManagerGetDevicesResponse(BaseModel):
    Devices: list[NetworkManagerDevice] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
