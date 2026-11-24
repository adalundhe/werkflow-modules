from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyPublicIpDnsNameOptionsRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    HostnameType: Literal['public-dual-stack-dns-name', 'public-ipv4-dns-name', 'public-ipv6-dns-name']
    DryRun: StrictBool | None = None
