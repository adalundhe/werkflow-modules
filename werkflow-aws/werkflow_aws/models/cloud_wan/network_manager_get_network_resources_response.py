from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_network_resource import NetworkManagerNetworkResource


class NetworkManagerGetNetworkResourcesResponse(BaseModel):
    NetworkResources: list[NetworkManagerNetworkResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
