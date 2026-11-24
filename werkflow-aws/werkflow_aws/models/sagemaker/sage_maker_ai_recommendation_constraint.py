from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIRecommendationConstraint(BaseModel):
    Metric: StrictStr | None = None
