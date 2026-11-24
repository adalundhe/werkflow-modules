from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_security_group import EC2SecurityGroup


class EC2DescribeSecurityGroupsResponse(BaseModel):
    SecurityGroups: list[EC2SecurityGroup] | None = None
    NextToken: StrictStr | None = None
