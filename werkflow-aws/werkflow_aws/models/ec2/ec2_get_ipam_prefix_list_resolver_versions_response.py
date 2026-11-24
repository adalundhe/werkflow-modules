from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_prefix_list_resolver_version import EC2IpamPrefixListResolverVersion


class EC2GetIpamPrefixListResolverVersionsResponse(BaseModel):
    IpamPrefixListResolverVersions: list[EC2IpamPrefixListResolverVersion] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
