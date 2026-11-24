from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_context_store_association import NetworkManagerContextStoreAssociation


class NetworkManagerDisassociateContextStoreResponse(BaseModel):
    ContextStoreAssociation: NetworkManagerContextStoreAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
