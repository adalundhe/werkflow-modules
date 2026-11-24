from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateConnectionRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ConnectionId: StrictStr
    LinkId: StrictStr | None = None
    ConnectedLinkId: StrictStr | None = None
    Description: StrictStr | None = None
