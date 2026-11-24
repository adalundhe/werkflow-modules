from __future__ import annotations
from pydantic import BaseModel
from .rdsdb_cluster_snapshot import RDSDBClusterSnapshot


class RDSCreateDBClusterSnapshotResponse(BaseModel):
    DBClusterSnapshot: RDSDBClusterSnapshot | None = None
