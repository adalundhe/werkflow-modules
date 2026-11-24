from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_global_network import NetworkManagerGlobalNetwork


class NetworkManagerDescribeGlobalNetworksResponse(BaseModel):
    GlobalNetworks: list[NetworkManagerGlobalNetwork] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
