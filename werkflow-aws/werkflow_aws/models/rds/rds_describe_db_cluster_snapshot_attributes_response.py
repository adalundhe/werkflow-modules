from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_cluster_snapshot_attributes_result import RDSDBClusterSnapshotAttributesResult


class RDSDescribeDBClusterSnapshotAttributesResponse(BaseModel):
    DBClusterSnapshotAttributesResult: RDSDBClusterSnapshotAttributesResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
