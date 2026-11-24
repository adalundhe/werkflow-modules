from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_device import NetworkManagerDevice


class NetworkManagerCreateDeviceResponse(BaseModel):
    Device: NetworkManagerDevice | None = None
    ResponseMetadata: dict[str, Any] | None = None
