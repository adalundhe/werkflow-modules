from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2UnassignPrivateIpAddressesRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    Ipv4Prefixes: list[StrictStr] | None = None
    PrivateIpAddresses: list[StrictStr] | None = None
