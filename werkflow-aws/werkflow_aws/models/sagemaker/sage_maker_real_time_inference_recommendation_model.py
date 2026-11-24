from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRealTimeInferenceRecommendationModel(BaseModel):
    RecommendationId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
