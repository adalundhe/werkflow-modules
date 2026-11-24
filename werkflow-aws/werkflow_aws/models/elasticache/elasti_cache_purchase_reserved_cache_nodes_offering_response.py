from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_reserved_cache_node import ElastiCacheReservedCacheNode


class ElastiCachePurchaseReservedCacheNodesOfferingResponse(BaseModel):
    ReservedCacheNode: ElastiCacheReservedCacheNode | None = None
    ResponseMetadata: dict[str, Any] | None = None
