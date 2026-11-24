from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_security_group_for_vpc import EC2SecurityGroupForVpc


class EC2GetSecurityGroupsForVpcResponse(BaseModel):
    NextToken: StrictStr | None = None
    SecurityGroupForVpcs: list[EC2SecurityGroupForVpc] | None = None
    ResponseMetadata: dict[str, Any] | None = None
