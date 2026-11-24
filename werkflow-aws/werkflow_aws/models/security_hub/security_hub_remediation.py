from __future__ import annotations
from pydantic import BaseModel
from .security_hub_recommendation import SecurityHubRecommendation


class SecurityHubRemediation(BaseModel):
    Recommendation: SecurityHubRecommendation | None = None
