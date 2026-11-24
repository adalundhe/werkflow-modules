from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_transit_gateway_registration import NetworkManagerTransitGatewayRegistration


class NetworkManagerRegisterTransitGatewayResponse(BaseModel):
    TransitGatewayRegistration: NetworkManagerTransitGatewayRegistration | None = None
    ResponseMetadata: dict[str, Any] | None = None
