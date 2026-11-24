from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_security_group_reference import EC2SecurityGroupReference


class EC2DescribeSecurityGroupReferencesResponse(BaseModel):
    SecurityGroupReferenceSet: list[EC2SecurityGroupReference] | None = None
    ResponseMetadata: dict[str, Any] | None = None
