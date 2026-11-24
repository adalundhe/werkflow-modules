from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_reserved_cache_node import ElastiCacheReservedCacheNode


class ElastiCacheDescribeReservedCacheNodesResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedCacheNodes: list[ElastiCacheReservedCacheNode] | None = None
    ResponseMetadata: dict[str, Any] | None = None
