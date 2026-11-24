from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_security_group_rule_update import EC2SecurityGroupRuleUpdate


class EC2ModifySecurityGroupRulesRequest(BaseModel):
    GroupId: StrictStr
    SecurityGroupRules: list[EC2SecurityGroupRuleUpdate]
    DryRun: StrictBool | None = None
