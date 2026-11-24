from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster_snapshot import RDSDBClusterSnapshot


class RDSDescribeDBClusterSnapshotsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterSnapshots: list[RDSDBClusterSnapshot] | None = None
