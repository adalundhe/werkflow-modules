from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerRecommendationJobResourceLimit(BaseModel):
    MaxNumberOfTests: StrictInt | None = None
    MaxParallelOfTests: StrictInt | None = None
