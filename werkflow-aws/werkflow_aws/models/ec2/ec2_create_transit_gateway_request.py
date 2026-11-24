from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_transit_gateway_request_options import EC2TransitGatewayRequestOptions


class EC2CreateTransitGatewayRequest(BaseModel):
    Description: StrictStr | None = None
    Options: EC2TransitGatewayRequestOptions | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
