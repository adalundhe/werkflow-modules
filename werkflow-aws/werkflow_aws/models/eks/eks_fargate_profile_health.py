from __future__ import annotations
from pydantic import BaseModel
from .eks_fargate_profile_issue import EKSFargateProfileIssue


class EKSFargateProfileHealth(BaseModel):
    issues: list[EKSFargateProfileIssue] | None = None
