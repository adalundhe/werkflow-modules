from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_policy_rule import EC2TransitGatewayPolicyRule


class EC2TransitGatewayPolicyTableEntry(BaseModel):
    PolicyRuleNumber: StrictStr | None = None
    PolicyRule: EC2TransitGatewayPolicyRule | None = None
    TargetRouteTableId: StrictStr | None = None
    State: StrictStr | None = None
