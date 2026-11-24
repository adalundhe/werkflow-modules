from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_transit_gateway_peering import NetworkManagerTransitGatewayPeering


class NetworkManagerGetTransitGatewayPeeringResponse(BaseModel):
    TransitGatewayPeering: NetworkManagerTransitGatewayPeering | None = None
    ResponseMetadata: dict[str, Any] | None = None
