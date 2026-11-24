from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_multicast_domain_associations import EC2TransitGatewayMulticastDomainAssociations


class EC2DisassociateTransitGatewayMulticastDomainResponse(BaseModel):
    Associations: EC2TransitGatewayMulticastDomainAssociations | None = None
    ResponseMetadata: dict[str, Any] | None = None
