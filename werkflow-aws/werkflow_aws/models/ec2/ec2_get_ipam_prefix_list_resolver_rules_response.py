from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_prefix_list_resolver_rule import EC2IpamPrefixListResolverRule


class EC2GetIpamPrefixListResolverRulesResponse(BaseModel):
    Rules: list[EC2IpamPrefixListResolverRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
