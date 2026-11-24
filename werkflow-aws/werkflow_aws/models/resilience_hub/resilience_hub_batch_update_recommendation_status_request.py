from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_update_recommendation_status_request_entry import ResilienceHubUpdateRecommendationStatusRequestEntry


class ResilienceHubBatchUpdateRecommendationStatusRequest(BaseModel):
    appArn: StrictStr
    requestEntries: list[ResilienceHubUpdateRecommendationStatusRequestEntry]
