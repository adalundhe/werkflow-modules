from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAssociateConnectPeerRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ConnectPeerId: StrictStr
    DeviceId: StrictStr
    LinkId: StrictStr | None = None
