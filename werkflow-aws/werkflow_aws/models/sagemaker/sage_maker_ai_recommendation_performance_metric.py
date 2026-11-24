from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIRecommendationPerformanceMetric(BaseModel):
    Metric: StrictStr | None = None
    Stat: StrictStr | None = None
    Value: StrictStr | None = None
    Unit: StrictStr | None = None
