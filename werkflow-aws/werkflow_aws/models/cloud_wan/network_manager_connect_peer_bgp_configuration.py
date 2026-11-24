from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerConnectPeerBgpConfiguration(BaseModel):
    CoreNetworkAsn: StrictInt | None = None
    PeerAsn: StrictInt | None = None
    CoreNetworkAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
