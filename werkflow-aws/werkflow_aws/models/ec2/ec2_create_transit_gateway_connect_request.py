from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_transit_gateway_connect_request_options import EC2CreateTransitGatewayConnectRequestOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateTransitGatewayConnectRequest(BaseModel):
    TransportTransitGatewayAttachmentId: StrictStr
    Options: EC2CreateTransitGatewayConnectRequestOptions
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
