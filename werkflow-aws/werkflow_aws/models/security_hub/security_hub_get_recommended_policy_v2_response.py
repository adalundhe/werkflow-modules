from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_recommendation_error import SecurityHubRecommendationError
from .security_hub_recommendation_step import SecurityHubRecommendationStep


class SecurityHubGetRecommendedPolicyV2Response(BaseModel):
    NextToken: StrictStr | None = None
    RecommendationType: StrictStr | None = None
    RecommendationSteps: list[SecurityHubRecommendationStep] | None = None
    Error: SecurityHubRecommendationError | None = None
    Status: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
