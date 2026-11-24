from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_nat_rule import EC2TransitGatewayNatRule


class EC2GetTransitGatewayAttachmentNatConfigurationResponse(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    NatGatewaySupport: StrictStr | None = None
    NatSystemRouteSupport: StrictStr | None = None
    NatGatewayRules: list[EC2TransitGatewayNatRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
