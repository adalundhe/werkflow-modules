from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerGetFindingRecommendationRequest(BaseModel):
    analyzerArn: StrictStr
    id: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
