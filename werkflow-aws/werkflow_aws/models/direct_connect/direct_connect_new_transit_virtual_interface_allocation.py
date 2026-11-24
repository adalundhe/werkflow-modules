from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectNewTransitVirtualInterfaceAllocation(BaseModel):
    virtualInterfaceName: StrictStr | None = None
    vlan: StrictInt | None = None
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    mtu: StrictInt | None = None
    authKey: StrictStr | None = None
    amazonAddress: StrictStr | None = None
    customerAddress: StrictStr | None = None
    addressFamily: Literal['ipv4', 'ipv6'] | None = None
    tags: list[DirectConnectTag] | None = None
    rateLimit: StrictStr | None = None
