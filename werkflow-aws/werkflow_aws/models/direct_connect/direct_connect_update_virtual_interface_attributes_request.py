from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DirectConnectUpdateVirtualInterfaceAttributesRequest(BaseModel):
    virtualInterfaceId: StrictStr
    mtu: StrictInt | None = None
    enableSiteLink: StrictBool | None = None
    virtualInterfaceName: StrictStr | None = None
    prefixPoolAllocatedCountIpv4: StrictInt | None = None
    prefixPoolAllocatedCountIpv6: StrictInt | None = None
    rateLimit: StrictStr | None = None
