from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .direct_connect_tag import DirectConnectTag


class DirectConnectCreateDirectConnectGatewayRequest(BaseModel):
    directConnectGatewayName: StrictStr
    tags: list[DirectConnectTag] | None = None
    amazonSideAsn: StrictInt | None = None
