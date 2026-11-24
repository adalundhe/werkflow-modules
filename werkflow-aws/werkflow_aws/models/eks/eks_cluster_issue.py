from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_cluster_issue_code import EKSClusterIssueCode


class EKSClusterIssue(BaseModel):
    code: EKSClusterIssueCode | None = None
    message: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
