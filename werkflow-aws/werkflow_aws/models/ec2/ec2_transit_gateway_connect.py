from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_connect_options import EC2TransitGatewayConnectOptions


class EC2TransitGatewayConnect(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    TransportTransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    State: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Options: EC2TransitGatewayConnectOptions | None = None
    Tags: list[EC2TagModel] | None = None
