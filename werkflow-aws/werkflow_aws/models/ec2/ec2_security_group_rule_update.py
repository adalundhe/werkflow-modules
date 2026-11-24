from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_security_group_rule_request import EC2SecurityGroupRuleRequest


class EC2SecurityGroupRuleUpdate(BaseModel):
    SecurityGroupRuleId: StrictStr
    SecurityGroupRule: EC2SecurityGroupRuleRequest | None = None
