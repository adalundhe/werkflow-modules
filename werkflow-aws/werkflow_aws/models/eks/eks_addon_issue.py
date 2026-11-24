from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_addon_issue_code import EKSAddonIssueCode


class EKSAddonIssue(BaseModel):
    code: EKSAddonIssueCode | None = None
    message: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
