from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_network_telemetry import NetworkManagerNetworkTelemetry


class NetworkManagerGetNetworkTelemetryResponse(BaseModel):
    NetworkTelemetry: list[NetworkManagerNetworkTelemetry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
