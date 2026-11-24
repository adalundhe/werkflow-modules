from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_cluster import MemoryDBCluster


class MemoryDBDescribeClustersResponse(BaseModel):
    NextToken: StrictStr | None = None
    Clusters: list[MemoryDBCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
