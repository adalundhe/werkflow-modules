from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_db_cluster_snapshot_attribute import NeptuneDBClusterSnapshotAttribute


class NeptuneDBClusterSnapshotAttributesResult(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr | None = None
    DBClusterSnapshotAttributes: list[NeptuneDBClusterSnapshotAttribute] | None = None
