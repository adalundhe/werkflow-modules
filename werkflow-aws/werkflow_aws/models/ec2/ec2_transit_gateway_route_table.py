from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TransitGatewayRouteTable(BaseModel):
    TransitGatewayRouteTableId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    State: StrictStr | None = None
    DefaultAssociationRouteTable: StrictBool | None = None
    DefaultPropagationRouteTable: StrictBool | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
