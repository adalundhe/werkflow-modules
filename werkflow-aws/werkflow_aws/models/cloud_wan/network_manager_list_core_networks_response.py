from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_summary import NetworkManagerCoreNetworkSummary


class NetworkManagerListCoreNetworksResponse(BaseModel):
    CoreNetworks: list[NetworkManagerCoreNetworkSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
