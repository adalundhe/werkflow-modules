from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ec2_ipam_prefix_list_resolver_rule_condition_request import EC2IpamPrefixListResolverRuleConditionRequest


class EC2IpamPrefixListResolverRuleRequest(BaseModel):
    RuleType: Literal['static-cidr', 'ipam-resource-cidr', 'ipam-pool-cidr']
    StaticCidr: StrictStr | None = None
    IpamScopeId: StrictStr | None = None
    ResourceType: Literal['vpc', 'subnet', 'eip', 'public-ipv4-pool', 'ipv6-pool', 'eni', 'anycast-ip-list'] | None = None
    Conditions: list[EC2IpamPrefixListResolverRuleConditionRequest] | None = None
