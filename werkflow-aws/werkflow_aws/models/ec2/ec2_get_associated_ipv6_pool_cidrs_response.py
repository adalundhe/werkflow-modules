from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipv6_cidr_association import EC2Ipv6CidrAssociation


class EC2GetAssociatedIpv6PoolCidrsResponse(BaseModel):
    Ipv6CidrAssociations: list[EC2Ipv6CidrAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
