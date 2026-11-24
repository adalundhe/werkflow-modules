from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_security_group_vpc_association import EC2SecurityGroupVpcAssociation


class EC2DescribeSecurityGroupVpcAssociationsResponse(BaseModel):
    SecurityGroupVpcAssociations: list[EC2SecurityGroupVpcAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
