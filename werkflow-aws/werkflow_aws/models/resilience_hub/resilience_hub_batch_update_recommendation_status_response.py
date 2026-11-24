from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_batch_update_recommendation_status_failed_entry import ResilienceHubBatchUpdateRecommendationStatusFailedEntry
from .resilience_hub_batch_update_recommendation_status_successful_entry import ResilienceHubBatchUpdateRecommendationStatusSuccessfulEntry


class ResilienceHubBatchUpdateRecommendationStatusResponse(BaseModel):
    appArn: StrictStr | None = None
    failedEntries: list[ResilienceHubBatchUpdateRecommendationStatusFailedEntry] | None = None
    successfulEntries: list[ResilienceHubBatchUpdateRecommendationStatusSuccessfulEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
