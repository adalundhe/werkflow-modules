from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_transit_gateway_request_policy_rule import EC2TransitGatewayRequestPolicyRule


class EC2CreateTransitGatewayPolicyTableEntryRequest(BaseModel):
    TransitGatewayPolicyTableId: StrictStr
    PolicyRuleNumber: StrictStr
    TargetRouteTableId: StrictStr
    PolicyRule: EC2TransitGatewayRequestPolicyRule | None = None
    DryRun: StrictBool | None = None
