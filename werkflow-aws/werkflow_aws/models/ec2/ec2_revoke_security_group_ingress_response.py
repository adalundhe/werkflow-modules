from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .ec2_ip_permission import EC2IpPermission
from .ec2_revoked_security_group_rule import EC2RevokedSecurityGroupRule


class EC2RevokeSecurityGroupIngressResponse(BaseModel):
    Return: StrictBool | None = None
    UnknownIpPermissions: list[EC2IpPermission] | None = None
    RevokedSecurityGroupRules: list[EC2RevokedSecurityGroupRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
