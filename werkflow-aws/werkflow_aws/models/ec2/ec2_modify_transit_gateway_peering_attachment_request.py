from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_modify_transit_gateway_peering_attachment_request_options import EC2ModifyTransitGatewayPeeringAttachmentRequestOptions


class EC2ModifyTransitGatewayPeeringAttachmentRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    Options: EC2ModifyTransitGatewayPeeringAttachmentRequestOptions | None = None
    DryRun: StrictBool | None = None
