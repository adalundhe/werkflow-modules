from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .resilience_hub_grouping_app_component import ResilienceHubGroupingAppComponent
from .resilience_hub_grouping_resource import ResilienceHubGroupingResource


class ResilienceHubGroupingRecommendation(BaseModel):
    confidenceLevel: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    groupingAppComponent: ResilienceHubGroupingAppComponent | None = None
    groupingRecommendationId: StrictStr | None = None
    recommendationReasons: list[StrictStr] | None = None
    rejectionReason: StrictStr | None = None
    resources: list[ResilienceHubGroupingResource] | None = None
    score: StrictFloat | StrictInt | None = None
    status: StrictStr | None = None
