from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_connect_peer import EC2TransitGatewayConnectPeer


class EC2CreateTransitGatewayConnectPeerResponse(BaseModel):
    TransitGatewayConnectPeer: EC2TransitGatewayConnectPeer | None = None
    ResponseMetadata: dict[str, Any] | None = None
