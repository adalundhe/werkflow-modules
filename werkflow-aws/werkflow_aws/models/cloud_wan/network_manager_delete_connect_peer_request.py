from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteConnectPeerRequest(BaseModel):
    ConnectPeerId: StrictStr
