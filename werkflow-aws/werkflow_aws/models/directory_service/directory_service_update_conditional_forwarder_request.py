from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceUpdateConditionalForwarderRequest(BaseModel):
    DirectoryId: StrictStr
    RemoteDomainName: StrictStr
    DnsIpAddrs: list[StrictStr] | None = None
    DnsIpv6Addrs: list[StrictStr] | None = None
