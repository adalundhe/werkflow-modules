from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_discovered_account import EC2IpamDiscoveredAccount


class EC2GetIpamDiscoveredAccountsResponse(BaseModel):
    IpamDiscoveredAccounts: list[EC2IpamDiscoveredAccount] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
