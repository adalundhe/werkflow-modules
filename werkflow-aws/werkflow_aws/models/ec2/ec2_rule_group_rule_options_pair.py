from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_rule_option import EC2RuleOption


class EC2RuleGroupRuleOptionsPair(BaseModel):
    RuleGroupArn: StrictStr | None = None
    RuleOptions: list[EC2RuleOption] | None = None
