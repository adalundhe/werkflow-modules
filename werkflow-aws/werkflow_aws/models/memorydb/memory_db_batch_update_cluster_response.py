from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_cluster import MemoryDBCluster
from .memory_db_unprocessed_cluster import MemoryDBUnprocessedCluster


class MemoryDBBatchUpdateClusterResponse(BaseModel):
    ProcessedClusters: list[MemoryDBCluster] | None = None
    UnprocessedClusters: list[MemoryDBUnprocessedCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
