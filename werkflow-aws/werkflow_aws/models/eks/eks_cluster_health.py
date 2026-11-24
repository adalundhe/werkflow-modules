from __future__ import annotations
from pydantic import BaseModel
from .eks_cluster_issue import EKSClusterIssue


class EKSClusterHealth(BaseModel):
    issues: list[EKSClusterIssue] | None = None
