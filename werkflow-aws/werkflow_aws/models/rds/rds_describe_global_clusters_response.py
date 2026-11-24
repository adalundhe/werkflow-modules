from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_global_cluster import RDSGlobalCluster


class RDSDescribeGlobalClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    GlobalClusters: list[RDSGlobalCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
