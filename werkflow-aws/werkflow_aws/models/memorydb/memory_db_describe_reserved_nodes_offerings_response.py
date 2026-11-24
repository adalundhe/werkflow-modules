from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_reserved_nodes_offering import MemoryDBReservedNodesOffering


class MemoryDBDescribeReservedNodesOfferingsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ReservedNodesOfferings: list[MemoryDBReservedNodesOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
