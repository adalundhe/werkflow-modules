from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_transit_gateway_nat_rule_request import EC2TransitGatewayNatRuleRequest


class EC2ModifyTransitGatewayAttachmentNatConfigurationRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    NatGatewaySupport: Literal['enable', 'disable'] | None = None
    NatSystemRouteSupport: Literal['enable', 'disable'] | None = None
    NatGatewayRules: list[EC2TransitGatewayNatRuleRequest] | None = None
    ResetNatGatewayRules: StrictBool | None = None
    DryRun: StrictBool | None = None
