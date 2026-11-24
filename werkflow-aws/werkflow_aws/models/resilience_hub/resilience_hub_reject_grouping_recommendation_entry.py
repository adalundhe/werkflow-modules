from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ResilienceHubRejectGroupingRecommendationEntry(BaseModel):
    groupingRecommendationId: StrictStr
    rejectionReason: Literal['DistinctBusinessPurpose', 'SeparateDataConcern', 'DistinctUserGroupHandling', 'Other'] | None = None
