from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_change_event import NetworkManagerCoreNetworkChangeEvent


class NetworkManagerGetCoreNetworkChangeEventsResponse(BaseModel):
    CoreNetworkChangeEvents: list[NetworkManagerCoreNetworkChangeEvent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
