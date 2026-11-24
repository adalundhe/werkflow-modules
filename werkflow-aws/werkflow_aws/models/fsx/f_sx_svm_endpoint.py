from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSvmEndpoint(BaseModel):
    DNSName: StrictStr | None = None
    IpAddresses: list[StrictStr] | None = None
    Ipv6Addresses: list[StrictStr] | None = None
