from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_context_store import NetworkManagerContextStore


class NetworkManagerCreateContextStoreResponse(BaseModel):
    ContextStore: NetworkManagerContextStore | None = None
    ResponseMetadata: dict[str, Any] | None = None
