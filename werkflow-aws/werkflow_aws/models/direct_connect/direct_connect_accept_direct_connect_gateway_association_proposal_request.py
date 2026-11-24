from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix


class DirectConnectAcceptDirectConnectGatewayAssociationProposalRequest(BaseModel):
    directConnectGatewayId: StrictStr
    proposalId: StrictStr
    associatedGatewayOwnerAccount: StrictStr
    overrideAllowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
