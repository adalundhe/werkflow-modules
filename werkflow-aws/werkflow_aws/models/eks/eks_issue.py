from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_nodegroup_issue_code import EKSNodegroupIssueCode


class EKSIssue(BaseModel):
    code: EKSNodegroupIssueCode | None = None
    message: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
