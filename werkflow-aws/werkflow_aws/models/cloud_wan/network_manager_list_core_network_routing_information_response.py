from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_routing_information import NetworkManagerCoreNetworkRoutingInformation


class NetworkManagerListCoreNetworkRoutingInformationResponse(BaseModel):
    CoreNetworkRoutingInformation: list[NetworkManagerCoreNetworkRoutingInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
