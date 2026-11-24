from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_batch_start_recommendations_error_entry import DMSBatchStartRecommendationsErrorEntry


class DMSBatchStartRecommendationsResponse(BaseModel):
    ErrorEntries: list[DMSBatchStartRecommendationsErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
