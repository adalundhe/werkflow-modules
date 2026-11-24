from __future__ import annotations
from pydantic import BaseModel
from .eks_addon_issue import EKSAddonIssue


class EKSAddonHealth(BaseModel):
    issues: list[EKSAddonIssue] | None = None
