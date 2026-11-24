from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_cluster import EMRCluster


class EMRDescribeClusterResponse(BaseModel):
    Cluster: EMRCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
