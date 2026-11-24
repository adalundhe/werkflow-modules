from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIRecommendationInferenceSpecification(BaseModel):
    Framework: StrictStr | None = None
