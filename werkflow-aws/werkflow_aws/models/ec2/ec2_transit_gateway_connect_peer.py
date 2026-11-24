from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_connect_peer_configuration import EC2TransitGatewayConnectPeerConfiguration


class EC2TransitGatewayConnectPeer(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayConnectPeerId: StrictStr | None = None
    State: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ConnectPeerConfiguration: EC2TransitGatewayConnectPeerConfiguration | None = None
    Tags: list[EC2TagModel] | None = None
