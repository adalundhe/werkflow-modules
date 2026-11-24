from __future__ import annotations
from pydantic import BaseModel
from .eks_cluster_issue_model import EKSClusterIssueModel


class EKSClusterHealthModel(BaseModel):
    issues: list[EKSClusterIssueModel] | None = None
