from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDisassociateConnectPeerRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ConnectPeerId: StrictStr
