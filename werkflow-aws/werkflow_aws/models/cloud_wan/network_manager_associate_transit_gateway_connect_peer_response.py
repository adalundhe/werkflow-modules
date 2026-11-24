from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_transit_gateway_connect_peer_association import NetworkManagerTransitGatewayConnectPeerAssociation


class NetworkManagerAssociateTransitGatewayConnectPeerResponse(BaseModel):
    TransitGatewayConnectPeerAssociation: NetworkManagerTransitGatewayConnectPeerAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
