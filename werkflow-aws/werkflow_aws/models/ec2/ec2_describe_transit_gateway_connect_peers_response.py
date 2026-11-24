from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_connect_peer import EC2TransitGatewayConnectPeer


class EC2DescribeTransitGatewayConnectPeersResponse(BaseModel):
    TransitGatewayConnectPeers: list[EC2TransitGatewayConnectPeer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
