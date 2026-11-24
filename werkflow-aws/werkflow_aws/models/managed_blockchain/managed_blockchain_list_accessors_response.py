from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_accessor_summary import ManagedBlockchainAccessorSummary


class ManagedBlockchainListAccessorsResponse(BaseModel):
    Accessors: list[ManagedBlockchainAccessorSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
