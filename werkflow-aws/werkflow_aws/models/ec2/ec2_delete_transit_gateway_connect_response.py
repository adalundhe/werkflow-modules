from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_connect import EC2TransitGatewayConnect


class EC2DeleteTransitGatewayConnectResponse(BaseModel):
    TransitGatewayConnect: EC2TransitGatewayConnect | None = None
    ResponseMetadata: dict[str, Any] | None = None
