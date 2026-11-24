from __future__ import annotations
from pydantic import BaseModel
from .eks_issue import EKSIssue


class EKSNodegroupHealth(BaseModel):
    issues: list[EKSIssue] | None = None
