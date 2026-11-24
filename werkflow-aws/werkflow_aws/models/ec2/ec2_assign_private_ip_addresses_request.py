from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2AssignPrivateIpAddressesRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    Ipv4Prefixes: list[StrictStr] | None = None
    Ipv4PrefixCount: StrictInt | None = None
    PrivateIpAddresses: list[StrictStr] | None = None
    SecondaryPrivateIpAddressCount: StrictInt | None = None
    AllowReassignment: StrictBool | None = None
