from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_context_store import NetworkManagerContextStore


class NetworkManagerListContextStoresResponse(BaseModel):
    ContextStores: list[NetworkManagerContextStore] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
