from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_policy_table_entry import EC2TransitGatewayPolicyTableEntry


class EC2ModifyTransitGatewayPolicyTableEntryResponse(BaseModel):
    TransitGatewayPolicyTableEntry: EC2TransitGatewayPolicyTableEntry | None = None
    ResponseMetadata: dict[str, Any] | None = None
