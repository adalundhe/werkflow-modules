from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_real_time_inference_recommendation import SageMakerRealTimeInferenceRecommendation
from .sage_maker_recommendation_status import SageMakerRecommendationStatus


class SageMakerDeploymentRecommendation(BaseModel):
    RecommendationStatus: SageMakerRecommendationStatus | None = None
    RealTimeInferenceRecommendations: list[SageMakerRealTimeInferenceRecommendation] | None = None
