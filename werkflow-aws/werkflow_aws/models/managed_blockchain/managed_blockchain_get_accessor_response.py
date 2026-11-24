from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .managed_blockchain_accessor import ManagedBlockchainAccessor


class ManagedBlockchainGetAccessorResponse(BaseModel):
    Accessor: ManagedBlockchainAccessor | None = None
    ResponseMetadata: dict[str, Any] | None = None
