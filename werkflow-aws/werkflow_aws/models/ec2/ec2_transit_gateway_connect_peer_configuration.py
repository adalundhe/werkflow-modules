from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_attachment_bgp_configuration import EC2TransitGatewayAttachmentBgpConfiguration


class EC2TransitGatewayConnectPeerConfiguration(BaseModel):
    TransitGatewayAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
    InsideCidrBlocks: list[StrictStr] | None = None
    Protocol: StrictStr | None = None
    BgpConfigurations: list[EC2TransitGatewayAttachmentBgpConfiguration] | None = None
