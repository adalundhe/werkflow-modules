from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_subnet_association import EC2SubnetAssociation


class EC2TransitGatewayMulticastDomainAssociations(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    Subnets: list[EC2SubnetAssociation] | None = None
