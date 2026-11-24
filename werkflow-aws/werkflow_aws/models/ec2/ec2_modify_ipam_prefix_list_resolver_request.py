from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_ipam_prefix_list_resolver_rule_request import EC2IpamPrefixListResolverRuleRequest


class EC2ModifyIpamPrefixListResolverRequest(BaseModel):
    IpamPrefixListResolverId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    Rules: list[EC2IpamPrefixListResolverRuleRequest] | None = None
