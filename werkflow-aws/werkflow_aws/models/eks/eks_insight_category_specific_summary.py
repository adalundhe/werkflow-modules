from __future__ import annotations
from pydantic import BaseModel
from .eks_addon_compatibility_detail import EKSAddonCompatibilityDetail
from .eks_deprecation_detail import EKSDeprecationDetail


class EKSInsightCategorySpecificSummary(BaseModel):
    deprecationDetails: list[EKSDeprecationDetail] | None = None
    addonCompatibilityDetails: list[EKSAddonCompatibilityDetail] | None = None
