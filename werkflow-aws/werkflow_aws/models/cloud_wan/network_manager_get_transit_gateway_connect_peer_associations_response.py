from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_transit_gateway_connect_peer_association import NetworkManagerTransitGatewayConnectPeerAssociation


class NetworkManagerGetTransitGatewayConnectPeerAssociationsResponse(BaseModel):
    TransitGatewayConnectPeerAssociations: list[NetworkManagerTransitGatewayConnectPeerAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
