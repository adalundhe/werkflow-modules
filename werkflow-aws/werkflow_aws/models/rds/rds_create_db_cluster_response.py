from __future__ import annotations
from pydantic import BaseModel
from .rdsdb_cluster import RDSDBCluster


class RDSCreateDBClusterResponse(BaseModel):
    DBCluster: RDSDBCluster | None = None
