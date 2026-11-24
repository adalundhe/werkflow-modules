from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_associated_core_network import DirectConnectAssociatedCoreNetwork
from .direct_connect_associated_gateway import DirectConnectAssociatedGateway
from .direct_connect_route_filter_prefix import DirectConnectRouteFilterPrefix


class DirectConnectGatewayAssociation(BaseModel):
    directConnectGatewayId: StrictStr | None = None
    directConnectGatewayOwnerAccount: StrictStr | None = None
    associationState: StrictStr | None = None
    stateChangeError: StrictStr | None = None
    associatedGateway: DirectConnectAssociatedGateway | None = None
    associationId: StrictStr | None = None
    allowedPrefixesToDirectConnectGateway: list[DirectConnectRouteFilterPrefix] | None = None
    associatedCoreNetwork: DirectConnectAssociatedCoreNetwork | None = None
    virtualGatewayId: StrictStr | None = None
    virtualGatewayRegion: StrictStr | None = None
    virtualGatewayOwnerAccount: StrictStr | None = None
