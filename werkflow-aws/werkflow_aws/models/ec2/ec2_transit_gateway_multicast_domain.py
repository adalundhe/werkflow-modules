from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_multicast_domain_options import EC2TransitGatewayMulticastDomainOptions


class EC2TransitGatewayMulticastDomain(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    TransitGatewayMulticastDomainArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Options: EC2TransitGatewayMulticastDomainOptions | None = None
    State: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
