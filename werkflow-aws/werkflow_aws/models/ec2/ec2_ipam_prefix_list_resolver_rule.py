from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ipam_prefix_list_resolver_rule_condition import EC2IpamPrefixListResolverRuleCondition


class EC2IpamPrefixListResolverRule(BaseModel):
    RuleType: StrictStr | None = None
    StaticCidr: StrictStr | None = None
    IpamScopeId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Conditions: list[EC2IpamPrefixListResolverRuleCondition] | None = None
