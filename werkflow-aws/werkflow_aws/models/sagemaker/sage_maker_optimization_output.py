from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOptimizationOutput(BaseModel):
    RecommendedInferenceImage: StrictStr | None = None
