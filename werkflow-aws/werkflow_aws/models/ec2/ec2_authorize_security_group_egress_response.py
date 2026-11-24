from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .ec2_security_group_rule import EC2SecurityGroupRule


class EC2AuthorizeSecurityGroupEgressResponse(BaseModel):
    Return: StrictBool | None = None
    SecurityGroupRules: list[EC2SecurityGroupRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
