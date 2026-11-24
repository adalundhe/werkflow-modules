from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_vpc_attachment import EC2VpcAttachment


class EC2VpnGateway(BaseModel):
    AmazonSideAsn: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
    VpnGatewayId: StrictStr | None = None
    State: StrictStr | None = None
    Type: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    VpcAttachments: list[EC2VpcAttachment] | None = None
