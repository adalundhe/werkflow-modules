from __future__ import annotations
from pydantic import BaseModel
from .msk_cluster_v2 import MSKClusterV2


class MSKDescribeClusterV2Response(BaseModel):
    ClusterInfo: MSKClusterV2 | None = None
