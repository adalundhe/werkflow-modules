from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_peering import NetworkManagerPeering


class NetworkManagerDeletePeeringResponse(BaseModel):
    Peering: NetworkManagerPeering | None = None
    ResponseMetadata: dict[str, Any] | None = None
