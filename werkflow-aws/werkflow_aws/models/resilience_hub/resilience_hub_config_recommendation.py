from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_cost import ResilienceHubCost
from .resilience_hub_disruption_compliance import ResilienceHubDisruptionCompliance
from .resilience_hub_recommendation_disruption_compliance import ResilienceHubRecommendationDisruptionCompliance


class ResilienceHubConfigRecommendation(BaseModel):
    appComponentName: StrictStr | None = None
    compliance: dict[StrictStr, ResilienceHubDisruptionCompliance] | None = None
    cost: ResilienceHubCost | None = None
    description: StrictStr | None = None
    haArchitecture: StrictStr | None = None
    name: StrictStr | None = None
    optimizationType: StrictStr | None = None
    recommendationCompliance: dict[StrictStr, ResilienceHubRecommendationDisruptionCompliance] | None = None
    referenceId: StrictStr | None = None
    suggestedChanges: list[StrictStr] | None = None
