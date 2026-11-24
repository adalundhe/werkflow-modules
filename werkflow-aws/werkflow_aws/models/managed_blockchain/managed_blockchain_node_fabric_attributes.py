from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainNodeFabricAttributes(BaseModel):
    PeerEndpoint: StrictStr | None = None
    PeerEventEndpoint: StrictStr | None = None
