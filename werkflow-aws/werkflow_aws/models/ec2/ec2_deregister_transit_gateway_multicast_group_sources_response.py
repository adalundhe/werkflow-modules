from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_multicast_deregistered_group_sources import EC2TransitGatewayMulticastDeregisteredGroupSources


class EC2DeregisterTransitGatewayMulticastGroupSourcesResponse(BaseModel):
    DeregisteredMulticastGroupSources: EC2TransitGatewayMulticastDeregisteredGroupSources | None = None
    ResponseMetadata: dict[str, Any] | None = None
