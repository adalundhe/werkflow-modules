from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_cidr_block_association import SecurityHubCidrBlockAssociation
from .security_hub_ipv6_cidr_block_association import SecurityHubIpv6CidrBlockAssociation


class SecurityHubAwsEc2VpcDetails(BaseModel):
    CidrBlockAssociationSet: list[SecurityHubCidrBlockAssociation] | None = None
    Ipv6CidrBlockAssociationSet: list[SecurityHubIpv6CidrBlockAssociation] | None = None
    DhcpOptionsId: StrictStr | None = None
    State: StrictStr | None = None
