from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectNewPrivateVirtualInterface(BaseModel):
    virtualInterfaceName: StrictStr
    vlan: StrictInt
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    mtu: StrictInt | None = None
    authKey: StrictStr | None = None
    amazonAddress: StrictStr | None = None
    customerAddress: StrictStr | None = None
    addressFamily: Literal['ipv4', 'ipv6'] | None = None
    virtualGatewayId: StrictStr | None = None
    directConnectGatewayId: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    enableSiteLink: StrictBool | None = None
    prefixPoolAllocatedCountIpv4: StrictInt | None = None
    prefixPoolAllocatedCountIpv6: StrictInt | None = None
    rateLimit: StrictStr | None = None
