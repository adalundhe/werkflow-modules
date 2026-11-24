from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_transit_gateway_route_table_attachment import NetworkManagerTransitGatewayRouteTableAttachment


class NetworkManagerGetTransitGatewayRouteTableAttachmentResponse(BaseModel):
    TransitGatewayRouteTableAttachment: NetworkManagerTransitGatewayRouteTableAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
