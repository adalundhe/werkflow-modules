from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerGenerateFindingRecommendationRequest(BaseModel):
    analyzerArn: StrictStr
    id: StrictStr
