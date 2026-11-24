from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2UnassignIpv6AddressesRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    Ipv6Prefixes: list[StrictStr] | None = None
    Ipv6Addresses: list[StrictStr] | None = None
