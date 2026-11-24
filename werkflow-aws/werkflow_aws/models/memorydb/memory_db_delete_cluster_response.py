from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_cluster import MemoryDBCluster


class MemoryDBDeleteClusterResponse(BaseModel):
    Cluster: MemoryDBCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
