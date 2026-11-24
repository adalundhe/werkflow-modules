from __future__ import annotations
from pydantic import BaseModel
from .rdsdb_cluster import RDSDBCluster


class RDSDeleteDBClusterResponse(BaseModel):
    DBCluster: RDSDBCluster | None = None
