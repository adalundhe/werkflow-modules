from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_transit_gateway_multicast_domain_request_options import EC2CreateTransitGatewayMulticastDomainRequestOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateTransitGatewayMulticastDomainRequest(BaseModel):
    TransitGatewayId: StrictStr
    Options: EC2CreateTransitGatewayMulticastDomainRequestOptions | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
