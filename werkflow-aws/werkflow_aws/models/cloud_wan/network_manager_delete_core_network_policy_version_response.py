from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_core_network_policy import NetworkManagerCoreNetworkPolicy


class NetworkManagerDeleteCoreNetworkPolicyVersionResponse(BaseModel):
    CoreNetworkPolicy: NetworkManagerCoreNetworkPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
