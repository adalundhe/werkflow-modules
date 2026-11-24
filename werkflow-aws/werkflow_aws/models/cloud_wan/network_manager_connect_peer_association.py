from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerConnectPeerAssociation(BaseModel):
    ConnectPeerId: StrictStr | None = None
    GlobalNetworkId: StrictStr | None = None
    DeviceId: StrictStr | None = None
    LinkId: StrictStr | None = None
    State: StrictStr | None = None
