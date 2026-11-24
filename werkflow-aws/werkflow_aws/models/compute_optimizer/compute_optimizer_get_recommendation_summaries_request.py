from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComputeOptimizerGetRecommendationSummariesRequest(BaseModel):
    accountIds: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
