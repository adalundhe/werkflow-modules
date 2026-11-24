from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteClusterPeerRequest(BaseModel):
    ClusterPeerId: StrictStr
    ClientRequestToken: StrictStr | None = None
