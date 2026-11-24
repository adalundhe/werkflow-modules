from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteConnectionRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ConnectionId: StrictStr
