from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .resilience_hub_update_recommendation_status_item import ResilienceHubUpdateRecommendationStatusItem


class ResilienceHubBatchUpdateRecommendationStatusSuccessfulEntry(BaseModel):
    appComponentId: StrictStr | None = None
    entryId: StrictStr | None = None
    excludeReason: StrictStr | None = None
    excluded: StrictBool | None = None
    item: ResilienceHubUpdateRecommendationStatusItem | None = None
    referenceId: StrictStr | None = None
