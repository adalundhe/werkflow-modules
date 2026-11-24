from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_transit_gateway_vpc_attachment_request_options import EC2CreateTransitGatewayVpcAttachmentRequestOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateTransitGatewayVpcAttachmentRequest(BaseModel):
    TransitGatewayId: StrictStr
    VpcId: StrictStr
    SubnetIds: list[StrictStr]
    Options: EC2CreateTransitGatewayVpcAttachmentRequestOptions | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
