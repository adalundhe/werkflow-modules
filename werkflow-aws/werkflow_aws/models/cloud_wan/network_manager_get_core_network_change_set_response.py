from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_change import NetworkManagerCoreNetworkChange


class NetworkManagerGetCoreNetworkChangeSetResponse(BaseModel):
    CoreNetworkChanges: list[NetworkManagerCoreNetworkChange] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
