from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_modify_transit_gateway_vpc_attachment_request_options import EC2ModifyTransitGatewayVpcAttachmentRequestOptions


class EC2ModifyTransitGatewayVpcAttachmentRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    AddSubnetIds: list[StrictStr] | None = None
    RemoveSubnetIds: list[StrictStr] | None = None
    Options: EC2ModifyTransitGatewayVpcAttachmentRequestOptions | None = None
    DryRun: StrictBool | None = None
