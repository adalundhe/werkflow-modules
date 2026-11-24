from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2RouteServerBgpOptions(BaseModel):
    PeerAsn: StrictInt | None = None
    PeerLivenessDetection: StrictStr | None = None
