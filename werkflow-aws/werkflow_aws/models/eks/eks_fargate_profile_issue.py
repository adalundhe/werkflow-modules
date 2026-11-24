from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_fargate_profile_issue_code import EKSFargateProfileIssueCode


class EKSFargateProfileIssue(BaseModel):
    code: EKSFargateProfileIssueCode | None = None
    message: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
