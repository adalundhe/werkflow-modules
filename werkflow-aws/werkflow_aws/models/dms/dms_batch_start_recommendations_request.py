from __future__ import annotations
from pydantic import BaseModel
from .dms_start_recommendations_request_entry import DMSStartRecommendationsRequestEntry


class DMSBatchStartRecommendationsRequest(BaseModel):
    Data: list[DMSStartRecommendationsRequestEntry] | None = None
