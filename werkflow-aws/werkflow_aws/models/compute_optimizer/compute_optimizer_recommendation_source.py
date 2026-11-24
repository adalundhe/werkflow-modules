from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerRecommendationSource(BaseModel):
    recommendationSourceArn: StrictStr | None = None
    recommendationSourceType: StrictStr | None = None
