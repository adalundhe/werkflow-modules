from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIRecommendationOptimizationDetail(BaseModel):
    OptimizationType: StrictStr | None = None
    OptimizationConfig: dict[StrictStr, StrictStr] | None = None
