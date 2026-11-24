from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .resilience_hub_alarm import ResilienceHubAlarm
from .resilience_hub_experiment import ResilienceHubExperiment


class ResilienceHubRecommendationItem(BaseModel):
    alreadyImplemented: StrictBool | None = None
    discoveredAlarm: ResilienceHubAlarm | None = None
    excludeReason: StrictStr | None = None
    excluded: StrictBool | None = None
    latestDiscoveredExperiment: ResilienceHubExperiment | None = None
    resourceId: StrictStr | None = None
    targetAccountId: StrictStr | None = None
    targetRegion: StrictStr | None = None
