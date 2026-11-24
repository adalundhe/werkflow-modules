from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_multicast_group import EC2TransitGatewayMulticastGroup


class EC2SearchTransitGatewayMulticastGroupsResponse(BaseModel):
    MulticastGroups: list[EC2TransitGatewayMulticastGroup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
