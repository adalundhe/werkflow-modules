from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_blockchain_node_summary import ManagedBlockchainNodeSummary


class ManagedBlockchainListNodesResponse(BaseModel):
    Nodes: list[ManagedBlockchainNodeSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
