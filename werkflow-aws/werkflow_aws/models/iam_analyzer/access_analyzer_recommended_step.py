from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_unused_permissions_recommended_step import AccessAnalyzerUnusedPermissionsRecommendedStep


class AccessAnalyzerRecommendedStep(BaseModel):
    unusedPermissionsRecommendedStep: AccessAnalyzerUnusedPermissionsRecommendedStep | None = None
