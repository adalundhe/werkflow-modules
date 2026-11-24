from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_transit_gateway_request_policy_rule import EC2TransitGatewayRequestPolicyRule


class EC2ModifyTransitGatewayPolicyTableEntryRequest(BaseModel):
    TransitGatewayPolicyTableId: StrictStr
    PolicyRuleNumber: StrictStr
    PolicyRule: EC2TransitGatewayRequestPolicyRule | None = None
    TargetRouteTableId: StrictStr | None = None
    DryRun: StrictBool | None = None
