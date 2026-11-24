from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCancelDataQualityRuleRecommendationRunRequest(BaseModel):
    RunId: StrictStr
