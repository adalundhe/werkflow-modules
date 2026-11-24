from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_test_recommendation import ResilienceHubTestRecommendation


class ResilienceHubListTestRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    testRecommendations: list[ResilienceHubTestRecommendation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
