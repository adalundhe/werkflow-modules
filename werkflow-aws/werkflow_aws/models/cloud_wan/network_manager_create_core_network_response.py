from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_core_network import NetworkManagerCoreNetwork


class NetworkManagerCreateCoreNetworkResponse(BaseModel):
    CoreNetwork: NetworkManagerCoreNetwork | None = None
    ResponseMetadata: dict[str, Any] | None = None
