from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_blockchain_network import ManagedBlockchainNetwork


class ManagedBlockchainGetNetworkResponse(BaseModel):
    Network: ManagedBlockchainNetwork | None = None
    ResponseMetadata: dict[str, Any] | None = None
