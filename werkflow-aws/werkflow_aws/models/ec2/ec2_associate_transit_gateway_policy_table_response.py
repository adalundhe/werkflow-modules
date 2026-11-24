from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_policy_table_association import EC2TransitGatewayPolicyTableAssociation


class EC2AssociateTransitGatewayPolicyTableResponse(BaseModel):
    Association: EC2TransitGatewayPolicyTableAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
