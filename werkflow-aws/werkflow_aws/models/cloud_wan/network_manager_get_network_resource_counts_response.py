from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_network_resource_count import NetworkManagerNetworkResourceCount


class NetworkManagerGetNetworkResourceCountsResponse(BaseModel):
    NetworkResourceCounts: list[NetworkManagerNetworkResourceCount] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
