from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectGateway(BaseModel):
    directConnectGatewayId: StrictStr | None = None
    directConnectGatewayName: StrictStr | None = None
    amazonSideAsn: StrictInt | None = None
    ownerAccount: StrictStr | None = None
    directConnectGatewayState: StrictStr | None = None
    stateChangeError: StrictStr | None = None
    totalPrefixPoolAllocations: StrictInt | None = None
    tags: list[DirectConnectTag] | None = None
