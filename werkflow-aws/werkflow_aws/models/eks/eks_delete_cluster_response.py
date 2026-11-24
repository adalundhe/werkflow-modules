from __future__ import annotations
from pydantic import BaseModel
from .eks_cluster import EKSCluster


class EKSDeleteClusterResponse(BaseModel):
    cluster: EKSCluster | None = None
