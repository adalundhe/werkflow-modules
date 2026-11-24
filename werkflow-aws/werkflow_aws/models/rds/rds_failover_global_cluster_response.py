from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_global_cluster import RDSGlobalCluster


class RDSFailoverGlobalClusterResponse(BaseModel):
    GlobalCluster: RDSGlobalCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
