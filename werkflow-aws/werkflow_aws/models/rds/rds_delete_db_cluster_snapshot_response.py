from __future__ import annotations
from pydantic import BaseModel
from .rdsdb_cluster_snapshot import RDSDBClusterSnapshot


class RDSDeleteDBClusterSnapshotResponse(BaseModel):
    DBClusterSnapshot: RDSDBClusterSnapshot | None = None
