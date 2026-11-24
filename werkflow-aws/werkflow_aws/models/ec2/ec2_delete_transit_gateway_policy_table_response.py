from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_policy_table import EC2TransitGatewayPolicyTable


class EC2DeleteTransitGatewayPolicyTableResponse(BaseModel):
    TransitGatewayPolicyTable: EC2TransitGatewayPolicyTable | None = None
    ResponseMetadata: dict[str, Any] | None = None
