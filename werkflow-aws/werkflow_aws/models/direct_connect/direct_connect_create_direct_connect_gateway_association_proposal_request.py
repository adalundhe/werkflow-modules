from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix


class DirectConnectCreateDirectConnectGatewayAssociationProposalRequest(BaseModel):
    directConnectGatewayId: StrictStr
    directConnectGatewayOwnerAccount: StrictStr
    gatewayId: StrictStr
    addAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
    removeAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
