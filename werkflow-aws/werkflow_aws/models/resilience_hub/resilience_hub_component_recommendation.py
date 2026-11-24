from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_config_recommendation import ResilienceHubConfigRecommendation


class ResilienceHubComponentRecommendation(BaseModel):
    appComponentName: StrictStr | None = None
    configRecommendations: list[ResilienceHubConfigRecommendation] | None = None
    recommendationStatus: StrictStr | None = None
