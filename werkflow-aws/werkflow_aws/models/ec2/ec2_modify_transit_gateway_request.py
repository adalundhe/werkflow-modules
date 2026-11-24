from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_modify_transit_gateway_options import EC2ModifyTransitGatewayOptions


class EC2ModifyTransitGatewayRequest(BaseModel):
    TransitGatewayId: StrictStr
    Description: StrictStr | None = None
    Options: EC2ModifyTransitGatewayOptions | None = None
    DryRun: StrictBool | None = None
