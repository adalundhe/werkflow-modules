from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_peering_attachment_status import EC2PeeringAttachmentStatus
from .ec2_peering_tgw_info import EC2PeeringTgwInfo
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_peering_attachment_options import EC2TransitGatewayPeeringAttachmentOptions


class EC2TransitGatewayPeeringAttachment(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    AccepterTransitGatewayAttachmentId: StrictStr | None = None
    RequesterTgwInfo: EC2PeeringTgwInfo | None = None
    AccepterTgwInfo: EC2PeeringTgwInfo | None = None
    Options: EC2TransitGatewayPeeringAttachmentOptions | None = None
    Status: EC2PeeringAttachmentStatus | None = None
    State: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
