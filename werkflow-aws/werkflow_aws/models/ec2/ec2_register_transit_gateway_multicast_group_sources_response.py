from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_multicast_registered_group_sources import EC2TransitGatewayMulticastRegisteredGroupSources


class EC2RegisterTransitGatewayMulticastGroupSourcesResponse(BaseModel):
    RegisteredMulticastGroupSources: EC2TransitGatewayMulticastRegisteredGroupSources | None = None
    ResponseMetadata: dict[str, Any] | None = None
