from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeResourceGroupingRecommendationTaskRequest(BaseModel):
    appArn: StrictStr
    groupingId: StrictStr | None = None
