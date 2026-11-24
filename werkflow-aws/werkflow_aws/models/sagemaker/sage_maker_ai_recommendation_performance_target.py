from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ai_recommendation_constraint import SageMakerAIRecommendationConstraint


class SageMakerAIRecommendationPerformanceTarget(BaseModel):
    Constraints: list[SageMakerAIRecommendationConstraint] | None = None
