from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_multicast_domain import EC2TransitGatewayMulticastDomain


class EC2CreateTransitGatewayMulticastDomainResponse(BaseModel):
    TransitGatewayMulticastDomain: EC2TransitGatewayMulticastDomain | None = None
    ResponseMetadata: dict[str, Any] | None = None
