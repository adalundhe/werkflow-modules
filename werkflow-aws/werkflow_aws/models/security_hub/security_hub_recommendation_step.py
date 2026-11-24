from __future__ import annotations
from pydantic import BaseModel
from .security_hub_unused_permissions_recommendation_step import SecurityHubUnusedPermissionsRecommendationStep


class SecurityHubRecommendationStep(BaseModel):
    UnusedPermissions: SecurityHubUnusedPermissionsRecommendationStep | None = None
