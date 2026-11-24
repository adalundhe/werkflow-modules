from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_multicast_deregistered_group_members import EC2TransitGatewayMulticastDeregisteredGroupMembers


class EC2DeregisterTransitGatewayMulticastGroupMembersResponse(BaseModel):
    DeregisteredMulticastGroupMembers: EC2TransitGatewayMulticastDeregisteredGroupMembers | None = None
    ResponseMetadata: dict[str, Any] | None = None
