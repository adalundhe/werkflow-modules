from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_security_group_rule import EC2SecurityGroupRule


class EC2DescribeSecurityGroupRulesResponse(BaseModel):
    SecurityGroupRules: list[EC2SecurityGroupRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
