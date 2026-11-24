from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_vpc_attachment_options import EC2TransitGatewayVpcAttachmentOptions


class EC2TransitGatewayVpcAttachment(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    VpcId: StrictStr | None = None
    VpcOwnerId: StrictStr | None = None
    State: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Options: EC2TransitGatewayVpcAttachmentOptions | None = None
    Tags: list[EC2TagModel] | None = None
