from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix


class DirectConnectUpdateDirectConnectGatewayAssociationRequest(BaseModel):
    associationId: StrictStr | None = None
    addAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
    removeAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
