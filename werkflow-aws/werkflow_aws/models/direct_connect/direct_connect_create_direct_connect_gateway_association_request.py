from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix


class DirectConnectCreateDirectConnectGatewayAssociationRequest(BaseModel):
    directConnectGatewayId: StrictStr
    gatewayId: StrictStr | None = None
    addAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
    virtualGatewayId: StrictStr | None = None
