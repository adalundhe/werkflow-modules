from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_blockchain_node import ManagedBlockchainNode


class ManagedBlockchainGetNodeResponse(BaseModel):
    Node: ManagedBlockchainNode | None = None
    ResponseMetadata: dict[str, Any] | None = None
