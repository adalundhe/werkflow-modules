from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCachePurchaseReservedCacheNodesOfferingRequest(BaseModel):
    ReservedCacheNodesOfferingId: StrictStr
    ReservedCacheNodeId: StrictStr | None = None
    CacheNodeCount: StrictInt | None = None
    Tags: list[ElastiCacheTag] | None = None
