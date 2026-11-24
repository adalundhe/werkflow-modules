from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_reserved_node import MemoryDBReservedNode


class MemoryDBDescribeReservedNodesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ReservedNodes: list[MemoryDBReservedNode] | None = None
    ResponseMetadata: dict[str, Any] | None = None
