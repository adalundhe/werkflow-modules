from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubStartResourceGroupingRecommendationTaskRequest(BaseModel):
    appArn: StrictStr
