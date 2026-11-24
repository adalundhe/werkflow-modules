from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_options import EC2TransitGatewayOptions


class EC2TransitGateway(BaseModel):
    TransitGatewayId: StrictStr | None = None
    TransitGatewayArn: StrictStr | None = None
    State: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Options: EC2TransitGatewayOptions | None = None
    Tags: list[EC2TagModel] | None = None
