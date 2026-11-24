from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceConditionalForwarder(BaseModel):
    RemoteDomainName: StrictStr | None = None
    DnsIpAddrs: list[StrictStr] | None = None
    DnsIpv6Addrs: list[StrictStr] | None = None
    ReplicationScope: StrictStr | None = None
