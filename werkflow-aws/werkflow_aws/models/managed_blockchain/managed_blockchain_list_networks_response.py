from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_network_summary import ManagedBlockchainNetworkSummary


class ManagedBlockchainListNetworksResponse(BaseModel):
    Networks: list[ManagedBlockchainNetworkSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
