from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_cluster_snapshot_attributes_result import NeptuneDBClusterSnapshotAttributesResult


class NeptuneDescribeDBClusterSnapshotAttributesResponse(BaseModel):
    DBClusterSnapshotAttributesResult: NeptuneDBClusterSnapshotAttributesResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
