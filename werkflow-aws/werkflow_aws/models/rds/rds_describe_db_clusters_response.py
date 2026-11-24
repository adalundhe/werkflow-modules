from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster import RDSDBCluster


class RDSDescribeDBClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusters: list[RDSDBCluster] | None = None
