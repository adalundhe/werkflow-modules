from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_connection import NetworkManagerConnection


class NetworkManagerGetConnectionsResponse(BaseModel):
    Connections: list[NetworkManagerConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
