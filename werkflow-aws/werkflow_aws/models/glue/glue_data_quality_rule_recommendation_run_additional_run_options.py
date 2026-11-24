from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDataQualityRuleRecommendationRunAdditionalRunOptions(BaseModel):
    CustomLogGroupPrefix: StrictStr | None = None
