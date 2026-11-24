from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_peering import NetworkManagerPeering


class NetworkManagerListPeeringsResponse(BaseModel):
    Peerings: list[NetworkManagerPeering] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
