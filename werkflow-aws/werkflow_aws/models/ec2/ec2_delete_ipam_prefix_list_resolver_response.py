from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_prefix_list_resolver import EC2IpamPrefixListResolver


class EC2DeleteIpamPrefixListResolverResponse(BaseModel):
    IpamPrefixListResolver: EC2IpamPrefixListResolver | None = None
    ResponseMetadata: dict[str, Any] | None = None
