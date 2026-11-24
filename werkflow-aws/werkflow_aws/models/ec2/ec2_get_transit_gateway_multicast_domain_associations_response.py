from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_multicast_domain_association import EC2TransitGatewayMulticastDomainAssociation


class EC2GetTransitGatewayMulticastDomainAssociationsResponse(BaseModel):
    MulticastDomainAssociations: list[EC2TransitGatewayMulticastDomainAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
