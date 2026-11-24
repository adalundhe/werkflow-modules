from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_recommendation_item import ResilienceHubRecommendationItem


class ResilienceHubTestRecommendation(BaseModel):
    appComponentId: StrictStr | None = None
    appComponentName: StrictStr | None = None
    dependsOnAlarms: list[StrictStr] | None = None
    description: StrictStr | None = None
    intent: StrictStr | None = None
    items: list[ResilienceHubRecommendationItem] | None = None
    name: StrictStr | None = None
    prerequisite: StrictStr | None = None
    recommendationId: StrictStr | None = None
    recommendationStatus: StrictStr | None = None
    referenceId: StrictStr | None = None
    risk: StrictStr | None = None
    type: StrictStr | None = None
