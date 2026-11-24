from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_prefix_list_resolver_version_entry import EC2IpamPrefixListResolverVersionEntry


class EC2GetIpamPrefixListResolverVersionEntriesResponse(BaseModel):
    Entries: list[EC2IpamPrefixListResolverVersionEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
