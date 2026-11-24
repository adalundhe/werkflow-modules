from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerCoreNetworkSegmentEdgeIdentifier(BaseModel):
    CoreNetworkId: StrictStr | None = None
    SegmentName: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
