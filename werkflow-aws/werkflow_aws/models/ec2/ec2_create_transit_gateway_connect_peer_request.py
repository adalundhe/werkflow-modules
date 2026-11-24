from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_transit_gateway_connect_request_bgp_options import EC2TransitGatewayConnectRequestBgpOptions


class EC2CreateTransitGatewayConnectPeerRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    PeerAddress: StrictStr
    InsideCidrBlocks: list[StrictStr]
    TransitGatewayAddress: StrictStr | None = None
    BgpOptions: EC2TransitGatewayConnectRequestBgpOptions | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
