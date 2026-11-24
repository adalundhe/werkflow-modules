from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_ipam_prefix_list_resolver_rule_request import EC2IpamPrefixListResolverRuleRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamPrefixListResolverRequest(BaseModel):
    IpamId: StrictStr
    AddressFamily: Literal['ipv4', 'ipv6']
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    Rules: list[EC2IpamPrefixListResolverRuleRequest] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
