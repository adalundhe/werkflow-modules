from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster_snapshot_attribute import RDSDBClusterSnapshotAttribute


class RDSDBClusterSnapshotAttributesResult(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr | None = None
    DBClusterSnapshotAttributes: list[RDSDBClusterSnapshotAttribute] | None = None
