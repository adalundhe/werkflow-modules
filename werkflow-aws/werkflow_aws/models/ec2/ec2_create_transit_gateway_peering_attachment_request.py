from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_transit_gateway_peering_attachment_request_options import EC2CreateTransitGatewayPeeringAttachmentRequestOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateTransitGatewayPeeringAttachmentRequest(BaseModel):
    TransitGatewayId: StrictStr
    PeerTransitGatewayId: StrictStr
    PeerAccountId: StrictStr
    PeerRegion: StrictStr
    Options: EC2CreateTransitGatewayPeeringAttachmentRequestOptions | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
