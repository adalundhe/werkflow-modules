from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_associated_gateway import DirectConnectAssociatedGateway
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix


class DirectConnectGatewayAssociationProposal(BaseModel):
    proposalId: StrictStr | None = None
    directConnectGatewayId: StrictStr | None = None
    directConnectGatewayOwnerAccount: StrictStr | None = None
    proposalState: StrictStr | None = None
    associatedGateway: DirectConnectAssociatedGateway | None = None
    existingAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
    requestedAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
