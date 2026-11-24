from __future__ import annotations
from pydantic import BaseModel
from .eks_support_type import EKSSupportType


class EKSUpgradePolicyResponse(BaseModel):
    supportType: EKSSupportType | None = None
