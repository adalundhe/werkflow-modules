from __future__ import annotations
from pydantic import BaseModel
from .msk_cluster import MSKCluster


class MSKDescribeClusterResponse(BaseModel):
    ClusterInfo: MSKCluster | None = None
