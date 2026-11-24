from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_cluster_snapshot_model import RDSDBClusterSnapshotModel


class RDSCopyDBClusterSnapshotResponse(BaseModel):
    DBClusterSnapshot: RDSDBClusterSnapshotModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
