from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_reserved_cache_nodes_offering import ElastiCacheReservedCacheNodesOffering


class ElastiCacheDescribeReservedCacheNodesOfferingsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedCacheNodesOfferings: list[ElastiCacheReservedCacheNodesOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
