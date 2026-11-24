from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .resilience_hub_update_recommendation_status_item import ResilienceHubUpdateRecommendationStatusItem


class ResilienceHubUpdateRecommendationStatusRequestEntry(BaseModel):
    entryId: StrictStr
    excluded: StrictBool
    referenceId: StrictStr
    appComponentId: StrictStr | None = None
    excludeReason: Literal['AlreadyImplemented', 'NotRelevant', 'ComplexityOfImplementation'] | None = None
    item: ResilienceHubUpdateRecommendationStatusItem | None = None
