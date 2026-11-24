from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_multicast_registered_group_members import EC2TransitGatewayMulticastRegisteredGroupMembers


class EC2RegisterTransitGatewayMulticastGroupMembersResponse(BaseModel):
    RegisteredMulticastGroupMembers: EC2TransitGatewayMulticastRegisteredGroupMembers | None = None
    ResponseMetadata: dict[str, Any] | None = None
