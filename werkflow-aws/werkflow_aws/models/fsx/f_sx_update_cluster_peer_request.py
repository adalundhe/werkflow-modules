from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxUpdateClusterPeerRequest(BaseModel):
    ClusterPeerId: StrictStr
    ClientRequestToken: StrictStr | None = None
    PeerClusterName: StrictStr | None = None
    PeerAddresses: list[StrictStr] | None = None
