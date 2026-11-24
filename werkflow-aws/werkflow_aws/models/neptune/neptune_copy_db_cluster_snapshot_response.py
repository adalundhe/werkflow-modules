from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_cluster_snapshot import NeptuneDBClusterSnapshot


class NeptuneCopyDBClusterSnapshotResponse(BaseModel):
    DBClusterSnapshot: NeptuneDBClusterSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
