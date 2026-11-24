from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectNewPrivateVirtualInterfaceAllocation(BaseModel):
    virtualInterfaceName: StrictStr
    vlan: StrictInt
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    mtu: StrictInt | None = None
    authKey: StrictStr | None = None
    amazonAddress: StrictStr | None = None
    addressFamily: Literal['ipv4', 'ipv6'] | None = None
    customerAddress: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    rateLimit: StrictStr | None = None
