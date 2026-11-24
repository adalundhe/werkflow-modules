from __future__ import annotations
from pydantic import BaseModel
from .eks_capability_issue import EKSCapabilityIssue


class EKSCapabilityHealth(BaseModel):
    issues: list[EKSCapabilityIssue] | None = None
