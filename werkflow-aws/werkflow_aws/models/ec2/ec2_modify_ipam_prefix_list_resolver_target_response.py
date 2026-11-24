from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_prefix_list_resolver_target import EC2IpamPrefixListResolverTarget


class EC2ModifyIpamPrefixListResolverTargetResponse(BaseModel):
    IpamPrefixListResolverTarget: EC2IpamPrefixListResolverTarget | None = None
    ResponseMetadata: dict[str, Any] | None = None
