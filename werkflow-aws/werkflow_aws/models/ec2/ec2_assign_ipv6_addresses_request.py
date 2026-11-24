from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2AssignIpv6AddressesRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    Ipv6PrefixCount: StrictInt | None = None
    Ipv6Prefixes: list[StrictStr] | None = None
    Ipv6Addresses: list[StrictStr] | None = None
    Ipv6AddressCount: StrictInt | None = None
