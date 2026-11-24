from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_multicast_domain import EC2TransitGatewayMulticastDomain


class EC2DescribeTransitGatewayMulticastDomainsResponse(BaseModel):
    TransitGatewayMulticastDomains: list[EC2TransitGatewayMulticastDomain] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
