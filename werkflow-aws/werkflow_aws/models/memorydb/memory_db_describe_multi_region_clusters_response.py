from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_multi_region_cluster import MemoryDBMultiRegionCluster


class MemoryDBDescribeMultiRegionClustersResponse(BaseModel):
    NextToken: StrictStr | None = None
    MultiRegionClusters: list[MemoryDBMultiRegionCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
