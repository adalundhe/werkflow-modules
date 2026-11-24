from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_authorization_rule import EC2AuthorizationRule


class EC2DescribeClientVpnAuthorizationRulesResponse(BaseModel):
    AuthorizationRules: list[EC2AuthorizationRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
