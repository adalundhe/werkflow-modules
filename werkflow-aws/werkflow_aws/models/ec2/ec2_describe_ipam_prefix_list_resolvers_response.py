from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_prefix_list_resolver import EC2IpamPrefixListResolver


class EC2DescribeIpamPrefixListResolversResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamPrefixListResolvers: list[EC2IpamPrefixListResolver] | None = None
    ResponseMetadata: dict[str, Any] | None = None
