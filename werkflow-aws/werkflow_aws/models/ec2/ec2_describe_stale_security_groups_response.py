from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_stale_security_group import EC2StaleSecurityGroup


class EC2DescribeStaleSecurityGroupsResponse(BaseModel):
    NextToken: StrictStr | None = None
    StaleSecurityGroupSet: list[EC2StaleSecurityGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
