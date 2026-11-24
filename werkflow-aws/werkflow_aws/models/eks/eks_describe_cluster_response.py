from __future__ import annotations
from pydantic import BaseModel
from .eks_cluster import EKSCluster


class EKSDescribeClusterResponse(BaseModel):
    cluster: EKSCluster | None = None
