from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_attachment_association import EC2TransitGatewayAttachmentAssociation


class EC2TransitGatewayAttachment(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    TransitGatewayOwnerId: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    State: StrictStr | None = None
    Association: EC2TransitGatewayAttachmentAssociation | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    NatGatewaySupport: StrictStr | None = None
