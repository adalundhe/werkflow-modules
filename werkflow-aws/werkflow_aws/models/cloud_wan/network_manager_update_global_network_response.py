from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_global_network import NetworkManagerGlobalNetwork


class NetworkManagerUpdateGlobalNetworkResponse(BaseModel):
    GlobalNetwork: NetworkManagerGlobalNetwork | None = None
    ResponseMetadata: dict[str, Any] | None = None
