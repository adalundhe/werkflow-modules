from __future__ import annotations
from pydantic import BaseModel, StrictInt


class NetworkManagerBgpOptions(BaseModel):
    PeerAsn: StrictInt | None = None
