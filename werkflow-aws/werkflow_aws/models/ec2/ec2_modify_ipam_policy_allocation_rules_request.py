from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_ipam_policy_allocation_rule_request import EC2IpamPolicyAllocationRuleRequest


class EC2ModifyIpamPolicyAllocationRulesRequest(BaseModel):
    IpamPolicyId: StrictStr
    Locale: StrictStr
    ResourceType: Literal['alb', 'eip', 'rds', 'rnat', 'lambda-network-connector', 'igw-firewall']
    DryRun: StrictBool | None = None
    AllocationRules: list[EC2IpamPolicyAllocationRuleRequest] | None = None
