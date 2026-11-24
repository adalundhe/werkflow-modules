from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_connection import NetworkManagerConnection


class NetworkManagerDeleteConnectionResponse(BaseModel):
    Connection: NetworkManagerConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
