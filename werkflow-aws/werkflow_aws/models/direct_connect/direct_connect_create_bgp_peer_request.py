from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_bgp_peer import DirectConnectNewBGPPeer


class DirectConnectCreateBGPPeerRequest(BaseModel):
    virtualInterfaceId: StrictStr | None = None
    newBGPPeer: DirectConnectNewBGPPeer | None = None
