from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubFailedGroupingRecommendationEntry(BaseModel):
    errorMessage: StrictStr | None = None
    groupingRecommendationId: StrictStr | None = None
