from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateTransitGatewayRouteTableAnnouncementRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    PeeringAttachmentId: StrictStr
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
